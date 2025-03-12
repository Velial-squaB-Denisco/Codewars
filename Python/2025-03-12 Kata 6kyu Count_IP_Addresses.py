def ips_between(start ,end):
    
    i = 0
    j = 0

    startlist = str(start).split(".")
    endlist = str(end).split(".")

    print(startlist, endlist)

    for a in startlist:
        for pis in startlist:
            i += 256 - int(pis)
            print(i)

        for pis in endlist:
            j += 256 - int(pis)
            print(j)

        print("---")











    return i - j

print(ips_between("256.256.0.0", "256.256.1.0"))