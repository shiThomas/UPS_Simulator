def add_pickups(commands, truckid, whid, seqnum):
    pickup = commands.pickups.add()
    pickup.truckid = truckid
    pickup.whid = whid
    pickup.seqnum = seqnum
    return commands

def add_deliveries(command, truckid, packageid, x, y, seqnum):
    deliver = commands.deliveries.add()
    deliver.truckid = truckid
    package = deliver.packages.add()
    package.packageid = packageid
    package.x = x
    package.y = y
    deliver.seqnum = seqnum
    return commands

def add_queries(truckid, seqnum):
    query = commands.queries.add()
    query.truckid = truckid
    query.seqnum = seqnum
    return commands
