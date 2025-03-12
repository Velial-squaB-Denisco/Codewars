def ips_between(start ,end):
    
    i = 0
    j = 0

    startlist = str(start).split(".")
    endlist = str(end).split(".")

    print(startlist, endlist)

    for a in startlist:
        for pis in startlist:
            if pis % 256 == 1:
                pass
            print(pis)

        for pis in endlist:

            print(pis)

        print("---")











    return 0

print(ips_between("256.256.0.0", "256.256.1.0"))