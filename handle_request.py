import time
from ups import *
from build_commands import *
from build_ups_amazon_commands import *
from proto import ups_amazon_pb2

# Handle gopickups by evaluating commands from amazon
def execute_gopickups(amazon_socket, world_socket, warehouse, w_seq, ack_set):
    print('Inside execute_gopickups------------------------------------------')
    
    # Reply ack to Amazon
    return_ack_to_amazon(amazon_socket, warehouse.seqnum)
    
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
        desc = package.description
        truckid = -1
        while True:
            print('Selecting truck')
            # select an idle truck for picking up
            dbcursor.execute("select truck_id from myapp_truck where " +
                             "truck_status = " + str(idle) + " " +
                             "or truck_status = " + str(loaded) + " " +
                             "or truck_status = " + str(delivering) + " " +
                             "for update")
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
            "destination_x, destination_y, truckid, description) " +
            "values ('" +
            str(package_id) + "', '" +
            str(owner) + "', '" +
            str(0) + "', '" +
            str(x) + "', '" +
            str(y) + "', '" +
            str(truckid) +"', '" +
            desc+ "')")
        # print('After insert into package')

        # change status of truck to en route to warehouse
        dbcursor.execute(
            "update myapp_truck set " +
            "truck_status = " + str(traveling) +
            "where truck_id = '" + str(truckid) + "'")

    world_commands = world_ups_pb2.UCommands()
    add_pickups(world_commands, truckid, warehouse_id, w_seq)
    # world_commands.simspeed = 100

    print('Send UGopickup to world')
    print(world_commands)
    # print('Before receive ack from world')
    while w_seq not in ack_set:
        # print('Send UGopickup to world...')
        send_msg(world_socket, world_commands)
        time.sleep(sleep_time)
    # print('UGopickup: After receive ack from world')

    # ack_set.remove(w_seq)

    dbconn.commit()
    print('After commit')
    dbcursor.close()
    dbconn.close()
    
    # To do list:
    # 1. complete settleshipment response

#Before go delivery, receive msg from amz
def execute_godelivery(amazon_socket, world_socket, dest, w_seq, a_seq, ack_set):
    print('Inside execute_godelivery---------------------')
    
    #return ack number to amazon 
    return_ack_to_amazon(amazon_socket, dest.seqnum)
    
    for currtruck in dest.leavingtrucks:

        dbconn = connect_db()
        dbcursor = dbconn.cursor()

        
        world_commands = world_ups_pb2.UCommands()
        truckid = currtruck.truckid
        packageid = currtruck.packageid
        
        # need to add response command
        # print('packageid is:', packageid)
        dbcursor.execute(
            "select destination_x, destination_y " +
            "from myapp_package " +
            "where package_id = '" + str(packageid) + "'")
        package = dbcursor.fetchall()[0]
        x = package[0]
        y = package[1]
            
        #output command to world 
        
        # delivery_location = world_commands.packages.add()
        add_deliveries(world_commands, truckid, packageid, x, y, w_seq)
            
        #To do list:
        #1. SQL command to implement modifying package and truck status    !!!may not be necessary

        print('Send UGodelivery to world')
        print(world_commands)

        send_msg(world_socket, world_commands)
        
        #return settle msg to amazon
        print('Send settled to Amazon')
        ua_commands = ups_amazon_pb2.UACommands()
        add_settled(ua_commands,packageid,a_seq)
        a_seq+=1
        print(ua_commands)
        send_msg(amazon_socket,ua_commands)

        #update package status
        dbcursor.execute(
            "update myapp_package set " +
            "package_status = " + str(in_transit) + " "
            "where package_id = '" + str(packageid) + "'")

        
        while w_seq not in ack_set:
            # print('Send UGodivery to world again...')
            send_msg(world_socket, world_commands)
            time.sleep(sleep_time)
        # print('UGodelivery: After receive ack from world')
    
        # ack_set.remove(w_seq)        
        w_seq += 1

        dbcursor.execute(
            "update myapp_truck set " +
            "truck_status = " + str(delivering) + " "
            "where truck_id = '" + str(truckid) + "'")

        dbconn.commit()
        dbcursor.close()
        dbconn.close()

def handle_completion(amazon_socket, world_socket, completion, a_seq):
    print('Inside handle_completion()--------------------')
    
    # Reply ack to world
    return_ack_to_world(world_socket, completion.seqnum)

    # Connect to database
    dbconn = connect_db()
    dbcursor = dbconn.cursor()

    # Retrive data from completion
    truckid = completion.truckid
    wh_x = completion.x
    wh_y = completion.y
    status = completion.status

    # Query truck status from world
    # If status is 'idle', then change local database truck status to idle
    # Else, do the following things

    if status is 'IDLE':
        dbcursor.execute("update myapp_truck set " +
                     "truck_status = " + str(idle) + " " +
                     "where truck_id = '" + str(truckid) + "'")

    else:

    # Change the status of truck
        dbcursor.execute("update myapp_truck set " +
                         "truck_status = " + str(arrive_warehouse) +                          " " +
                         "where truck_id = '" + str(truckid) + "'")

        # Query package from database
        ua_commands = ups_amazon_pb2.UACommands()

        dbcursor.execute("select package_id from myapp_package where truckid = '"+str(truckid)+"' and package_status = '"+str(prepare_for_delivery)+"'")
        packages = dbcursor.fetchall()
        for package in packages:
            add_trucks(ua_commands, truckid, wh_x, wh_y, package[0], a_seq)
        a_seq += 1
        print('Send info to Amazon to notify the truck has arrived at warehouse')
        print(ua_commands)
        send_msg(amazon_socket, ua_commands)

    dbconn.commit()
    dbcursor.close()
    dbconn.close()

def handle_delivered(amazon_socket, world_socket, delivered, a_seq):
    print('Inside handle_delivered--------------------------')
    
    #Reply ack to world
    return_ack_to_world(world_socket, delivered.seqnum)

    #Receive data from delivered
    truckid = delivered.truckid
    packageid = delivered.packageid

    #update package status to delivered
    dbconn = connect_db()
    dbcursor = dbconn.cursor()
    dbcursor.execute("update myapp_package set "+
                     "package_status = '" + str(package_delivered) + "' "+
                     "where package_id = '" + str(packageid) + "'")

    ua_commands = ups_amazon_pb2.UACommands()
    add_finished(ua_commands, packageid, a_seq)
    print('Send finished/delivered info to Amazon')
    print(ua_commands)
    send_msg(amazon_socket, ua_commands)

    dbconn.commit()
    dbcursor.close()
    dbconn.close()

def handle_truckstatus(amazon_socket, world_socket, truckstatus):
    print('Inside handle_truckstatus()')
    
    #Reply ack to world
    return_ack_to_world(world_socket, truckstatus.seqnum)

    #print query msg
    print(truckstatus)

def handle_error(amazon_socket, world_socket, error):
    print('Inside handle_error')
    
    #Reply ack to world
    return_ack_to_world(world_socket, error.seqnum)

    #print error msg
    print("ERROR: ", error)
