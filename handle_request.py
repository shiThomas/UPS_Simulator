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

#Before go delivery, receive msg from amz
def execute_godelivery(amazon_socket,world_socket,dest,w_seq,a_seq):
    global ack_set
    
    #return ack number to amazon 
    return_ack_to_amazon(dest.seqnum)
    
    for currtruck in dest.leavingtrucks:

        dbconn = connect_db()
        dbcursor = dbconn.cursor()

        
        world_commands = world_ups_pb2.UCommands()
        truckid = currtruck.truckid
        packageid = currtruck.packageid
        
        #need to add response command
        dbcursor.execute("select destination_x,destination_y from package"+
                             " where package_id = '"+str(packageid)+"'")
        package = dbcursur.fetchall()[0]
        x = package[0]
        y = package[1]
            
        #output command to world 
        
        delivery_location = world_commands.packages.add()
        add_deliveries(delivery_location,truckid,packageid,x,y,w_seq)
            
        #To do list:
        #1. SQL command to implement modifying package and truck status    !!!may not be necessary

        while w_seq not in ack_set:
            print('Send UGopickup to world...')
            send_msg(world_socket, world_commands)
            time.sleep(sleep_time)
            print('After receive ack from world')
    
            ack_set.remove(w_seq)

        
        w_seq += 1

        dbcursor.execute(
            "update myapp_truck set " +
            "truck_status = " + str(delivering) +
            "where truck_id = '" + str(truckid) + "'")

        
        #return settle msg to amazon
        ua_commands = ups_amazon_pb2.UACommands()
        add_settled(ua_commands,packageid,a_seq)
        a_seq+=1


        send_msg(amazon_socket,ua_commands)

        
        dbconn.commit()
        print('After commit')
        dbcursor.close()
        dbconn.close()


