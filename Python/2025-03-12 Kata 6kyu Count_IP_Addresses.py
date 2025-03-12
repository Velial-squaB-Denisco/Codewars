def ips_between(start ,end):
    
    i = 0
    j = 0

    startlist = str(start).split(".")
    endlist = str(end).split(".")

    print(startlist, endlist)

  
    for pis in startlist:
        i += 256 - int(pis)
        print("i ", i, pis)

    for pis in endlist:
        j += 256 - int(pis)
        print("j ", j)

    print("---", a)











    return i - j

print(ips_between("256.256.0.0", "256.256.0.50"))