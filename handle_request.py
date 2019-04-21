
# Handle gopickups by evaluating commands from amazon
def execute_gopickups(amazon_socket,world_socket,commands):
    #Not sure if we need to keep track of tracking number
    trackingnum =[]
    for currpickup in commands.warehouses:
        warehouse_id = currpickup.whid
        wh_x =currpickup.wh_x
        wh_y = currpickup.wh_y
        
        for package in currpickup.packageinfos:
            package_list.append(package.packageid)
            #To do list: 
            #1. SQL command to implement insert to database
            #2. Figure out how to read status of package from tracking numebr and truck status
            #3. Fill gopickup command with the given axis coordinates 





#Before go delivery, command:ufinished
def execute_godelivery(amazon_socket,world_socket,commands):
    for currdeliver in commands.dests:
        for currtruck in currtruck.leavingtrucks:
            truckid = currtruck.truckid
            dest_x = currtruck.x
            dest_y = currtruck.y
            packageid = currtruck.packageid


            #To do list:
            #1. SQL command to implement modifying package and truck status
            

