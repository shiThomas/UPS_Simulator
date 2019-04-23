import time
from ups import *
from build_commands import *
from build_ups_amazon_commands import *
from proto import ups_amazon_pb2
    
def handle_completion(amazon_socket, world_socket, completion, a_seq):
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

    if status is 'idle':
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
        send_msg(amazon_socket, ua_commands)
    
    dbconn.commit()
    dbcursor.close()
    dbconn.close()
    
def handle_delivered(amazon_socket, world_socket, delivered, a_seq):
    #Reply ack to world
    return_ack_to_world(world_socket, delivered.seqnum)

    #Receive data from delivered
    truckid = delivered.truckid
    packageid = delivered.packageid    
    
    #update package status to delivered
    dbconn = connect_db()
    dbcursor = dbconn.cursor()
    dbcursor.execute("update myapp_package set "+
                     "package_status = "+str(delivered)+" "+
                     "where package_id ='"+str(packageid)+"'")

    ua_commands = ups_amazon_pb2.UACommands()
    add_finished(ua_commands, packageid, a_seq)
    send_msg(amazon_socket, ua_commands)

    dbconn.commit()
    dbcursor.close()
    dbconn.close()
    
def handle_truckstatus(amazon_socket, world_socket, truckstatus):
    #Reply ack to world
    return_ack_to_world(world_socket, delivered.seqnum)

    #print query msg
    print(truckstatus)
    
def handle_error(amazon_socket, world_socket, error):
    #Reply ack to world
    return_ack_to_world(world_socket, delivered.seqnum)

    #print error msg
    print("ERROR: ",error)
