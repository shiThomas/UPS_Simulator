def add_worlds(commands, worldid, seqnum):
    world = commands.worlds.add()
    world.worldid = worldid
    world.seqnum = seqnum
    return commands

def add_trucks(commands, truckid, x, y, packageid, seqnum):
    truck = commands.trucks.add()
    location = truck.arrivedtrucks.add()
    location.truckid = truckid
    location.wh_x = x
    location.wh_y = y
    location.packageid = packageid
    truck.seqnum = seqnum
    return commands

def add_settled(commands, packageid, seqnum):
    settle = commands.settled.add()
    settle.packageid[:] = [packageid]
    settle.seqnum = seqnum
    return commands

def add_finished(commands, packageid, seqnum):
    finished = commands.finished.add()
    finished.packageid[:] = [packageid]
    finished.seqnum = seqnum
    return commands
