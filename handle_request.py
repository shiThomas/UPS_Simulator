import time
from ups import *
from build_commands import *
from build_ups_amazon_commands import *
from proto import ups_amazon_pb2

# Handle gopickups by evaluating commands from amazon
def execute_gopickups(amazon_socket, world_socket, warehouse, w_seq):
    global ack_set

    # Reply ack to Amazon
    return_ack_to_amazon(warehouse.seqnum)
    
    # Connect to database
    dbconn = connect_db()
    dbcursor = dbconn.cursor()
    
    # Not sure if we need to keep track of tracking number
    trackingnum = []

    warehouse_id = warehouse.whid
    wh_x = warehouse.wh_x
    wh_y = warehouse.wh_y
    
    truckid = -1
    # package_list = []
    for package in warehouse.packageinfos:
        package_id = package.packageid
        # package_list.append(package_id)
        owner = package.upsaccount
        x = package.x
        y = package.y

        truckid = -1
        while True:
            # select an idle truck for picking up
            dbcursor.execute("select truck_id from myapp_truck where " +
                             "truck_status = " + str(idle) + " " +
                             "or truck_status = " + str(loaded) + " " +
                             "or truck_status = " + str(delivering))
            truck = dbcursor.fetchall()
            if len(truck) == 0:
                continue
            truckid = truck[0][0]
            print('truckid is:', truckid)
            break
            
        # add package_id, owner, package_status x, y to databse
        dbcursor.execute(
            "insert into myapp_package" +
            "(package_id, owner, package_status, " +
            "destination_x, destination_y, truckid) " +
            "values ('" +
            str(package_id) + "', '" +
            owner + "', '" +
            str(0) + "', '" +
            str(x) + "', '" +
            str(y) + "', '" +
            str(truckid) + "')")
        print('After insert into package')

        # change status of truck to en route to warehouse
        dbcursor.execute(
            "update myapp_truck set " +
            "truck_status = " + str(traveling) +
            "where truck_id = '" + str(truckid) + "'")

    world_commands = world_ups_pb2.UCommands()
    add_pickups(world_commands, truckid, warehouse_id, w_seq)
    world_commands.simspeed = 1000

    print('UGopickup commands')
    print(world_commands)
    print('Before receive ack from world')
    while w_seq not in ack_set:
        print('Send UGopickup to world...')
        send_msg(world_socket, world_commands)
        time.sleep(sleep_time)
    print('After receive ack from world')

    ack_set.remove(w_seq)

    dbconn.commit()
    print('After commit')
    dbcursor.close()
    dbconn.close()
    
    # To do list:
    # 1. complete settleshipment response

#Before go delivery, command:ufinished
def execute_godelivery(amazon_socket,world_socket,commands):
    for currdeliver in commands.dests:
        for currtruck in currtruck.leavingtrucks:
            truckid = currtruck.truckid
            packageid = currtruck.packageid
            
            #need to add response command
            dbcursor.execute("select * from Package where package_id = '"+str(packageid)+"')")
            package = dbcursur.fetchall()[0]
            x = package.x
            y = package.y
            
            #output_command not defined 
            
            add_deliveries(output_command,truckid,packageid,x,y)
            #To do list:
            #1. SQL command to implement modifying package and truck status    !!!may not be necessary
            
            


#To do list
#1. Deliverymade received, and respond to amz with a finish_shipment 

