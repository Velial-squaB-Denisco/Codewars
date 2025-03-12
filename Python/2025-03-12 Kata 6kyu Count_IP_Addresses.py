def ips_between(start ,end):
    
    i = 0
    j = 0

    startlist = str(start).split(".")
    endlist = str(end).split(".")

    print(startlist, endlist)

    for pis in startlist:

        print(pis)

    for pis in endlist:
        
        print(pis)











    return 0

print(ips_between("256.256.0.0", "256.256.1.0"))