def ips_between(start ,end):
    
    i = 0
    j = 0
    res = 0

    startlist = str(start).split(".")
    endlist = str(end).split(".")

    print(startlist, endlist)
  
    for pis in startlist[::-1]:
        i += int(pis)
        print("i ", i, pis)

    for pis in range(len(endlist[::-1])):
        if int(endlist[::-1][pis]) == 0:
            print("NULL")
        else:
            j += int(endlist[::-1][pis])
            print("j ", j, pis)

    print(i ," --- ", j)











    return j - i

print(ips_between("256.256.0.0", "256.256.1.0"))