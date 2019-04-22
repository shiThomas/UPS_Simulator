import time
from ups import *

# Handle gopickups by evaluating commands from amazon
def execute_gopickups(amazon_socket, world_socket, warehouse, a_seq, w_seq):
    # Connect to database
    dbconn = connect_db()
    dbcursor = dbconn.cursor()
    
    # Not sure if we need to keep track of tracking number
    trackingnum = []

    # dbcursor = db_conn.cursor()
    warehouse_id = warehouse.whid
    wh_x = warehouse.wh_x
    wh_y = warehouse.wh_y
    
    truckid = -1
    # package_list = []
    for package in warehouse.packageinfos:
        package_id = package.packageid
        # package_list.append(package_id)
        owner  = package.upsaccount
        x = package.x
        y = package.y

        # select an idle truck for picking up
        dbcursor.execute("select * from Trucks where truck_status = '"+str(1)+"'")
        truck = dbcursor.fetchall()[0]
            
        #add package_id, owner, package_status x, y to databse
            
        dbcursor.execute("insert into Package (package_id,owner,package_status,x,y,truck) values ('"
                             +str(package_id)+"', '"+owner+"', '"+str(0)+"', '" +x+"', '"+y+"', '"+str(truck.id)+"')")
        

        #change status of truck to en route to warehouse
        dbcursor.execute("update Truck set track_status = '"+str(2)+"' where truck_id ='"+str(truck.truck_id)+"')")
        truckid = truck.truck_id

    world_commands = world_ups_pb2.UCommands()
    add_pickups(world_commands, truckid, warehouse_id, w_seq)

    while w_seq not in ack_set:
        time.sleep(sleep_time)
        send_msg(world_socket, world_commands)

    ack_set.remove(w_seq)
    
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

