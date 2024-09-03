def getMinimumServer(servers, load):
    count = 0
    servers.sort(reverse=True)
    while count !=load :
        for num in servers:
            if num == load:
                count+=1

                

    return res
    