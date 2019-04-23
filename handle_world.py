import time
from ups import *
from build_commands import *
from build_ups_amazon_commands import *
from proto import ups_amazon_pb2
    
def handle_completion(amazon_socket, world_socket, completion, a_seq):
    # Reply ack to world
    return_ack_to_world(completion.seqnum)

    # Query truck status from world
    # If status is 'idle', then change local database truck status to idle
    # Else, do the following things
    
    # Connect to database
    dbconn = connect_db()
    dbcursor = dbconn.cursor()

    # Retrive data from completion
    truckid = completion.truckid
    wh_x = completion.x
    wh_y = completion.y
    status = completion.status

    # Change the status of truck
    dbcursor.execute("update myapp_truck set " +
                     "truck_status = " + str(arrive_warehouse) + " " +
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
    
def handle_delivered(amazon_socket, world_socket, delivered):
    
def handle_truckstatus(amazon_socket, world_socket, truckstatus):

def handle_error(amazon_socket, world_socket, error):
    
