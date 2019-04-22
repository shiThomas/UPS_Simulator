



    


# Handle gopickups by evaluating commands from amazon
def execute_gopickups(amazon_socket,world_socket,commands):
    #Not sure if we need to keep track of tracking number
    trackingnum =[]

    dbcursor = db_conn.cursor()
    for currpickup in commands.warehouses:
        warehouse_id = currpickup.whid
        wh_x =currpickup.wh_x
        wh_y = currpickup.wh_y
        
        truckid = -1
        for package in currpickup.packageinfos:
            package_list.append(package.packageid)
            package_id = package.packageid
            owner  = package.upsaccount
            x = package.x
            y = package.y

            #select a idle truck for picking up
            dbcursor.execute("select * from Truck where truck_status = '"+str(1)+"')")
            truck = dbcursor.fetchall()[0]
            
            #add package_id, owner, package_status x, y to databse
            
            dbcursor.execute("insert into Package (package_id,owner,package_status,x,y,truck) values ('"
                             +str(package_id)+"', '"+owner+"', '"+str(0)+"', '" +x+"', '"+y+"', '"+str(truck.id)+"')")
        

            #change status of truck to en route to warehouse
            dbcursor.execute("update Truck set track_status = '"+str(2)+"' where truck_id ='"+str(truck.truck_id)+"')")
            truckid = truck.truck_id


        add_pickups(output_command,truckid,warehouse_id)
            #To do list:
            #1. complete settleshipment response
           



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

