import socket
import time
import psycopg2

mySocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# EDIT: This line was added based on @Aleksander Gurin's response below. The problem persists.
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "vcm-8186.vm.duke.edu"
port = 1234
world_host = "World"
world_port = 12345
amazon_host=""
amazon_port=""


#To do list:
# 0. connect to Database.
# 1. connect to world.
# 2. initialize trucks
# 3. receive warehouse ID
# 4. Send go pick up signal to trucks
# 5. Receive Truck ID, WareHouse ID, Status from trucks
# 6. Send Truck ID to Amazon
# 7. Receive Destination ID and shipping location
# 8. Generate Package ID
# 9. Send go Deliver to trucks.


# Connect to Database.
while 1:
    try:
        dbconn = psycopg2.connect("dbname='portgres' user='postgres'"
                                  "host='' password=''")
        cur = dbconn.cursor()
        print "Successfully connected to the database"
        break
    except:
        print "Unable to connect to the database"
        continue
    
    
# Connect World

worldconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
worldconn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
while 1:
    try:
        worldconn.connect((world_host, world_port))
        print "Successfully connected to World"
        break
    except:
        print "Unable to connect to World"
        continue

# mySocket.bind( ('localhost', 1234 ) )


# mySocket.listen( 2 )

# channel, details = mySocket.accept()

# while True:

#     incoming = channel.recv( 100 )

#     if incoming: 
#         print "Received >%s<" % incoming
#         incoming = ''
        
