def ips_between(start ,end):
    
    i = 0
    j = 0

    startlist = str(start).split(".")
    endlist = str(end).split(".")

    print(startlist, endlist)

  
    for pis in startlist:
        if i - 256 == 0:
            i += 256
        else:
            i += 256 - int(pis)
        print("i ", i, "pis ", pis)

    for pis in range(len(endlist[::-1])):
        
        j += int(endlist[::-1][pis])
        print("j ", j, pis)

    print(i ," --- ", j)











    return j - i

print(ips_between("256.256.0.0", "256.256.1.0"))