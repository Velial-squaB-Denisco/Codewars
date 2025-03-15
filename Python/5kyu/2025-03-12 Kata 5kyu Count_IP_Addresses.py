def ips_between(start ,end):
    
    i = 0
    j = 0

    startlist = str(start).split(".")
    endlist = str(end).split(".")

    print(startlist, endlist)
  
    for pis in range(len(startlist)):
        print(3 - pis)
        i += int(startlist[pis]) * (256 ** (3 - pis))
        print("i ", i, pis)

    for pis in range(len(endlist)):
        print(3 - pis)
        j += int(endlist[pis]) * (256 ** (3 - pis))
        print("j ", j, pis)

    print(i ," --- ", j)

    return j - i

print(ips_between("256.256.0.0", "256.256.1.0"))