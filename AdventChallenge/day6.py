with open("input.txt") as f:
    data = f.read()
def p1and2(num=4): #Code I did after because this is better than my actual solutions
    items = [i for i in data]
    val = num
    while True:
        temp = items[:num]
        ret = True
        for i in temp:
            if temp.count(i) != 1:
                ret = False
        if ret:
            print(val)
            return(val)
        else:
            items.pop(0)
            val+=1
def p1():    
    #items = data.split()
    items = [i for i in data]
    print(items)
    marker = 4
    while True:
        i1 = items[0]
        i2 = items[1]
        i3 = items[2]
        i4 = items[3]
        if ((i1 not in items[1:4]) and (i2 not in items[2:5]) and (i3 not in items[3:6]) and (i4 not in items[4:7])):
            print(marker)
            return(marker)
        else:
            #print(i1,items[1:4])
            marker +=1
            items.pop(0)
def p2(): 
    items = [i for i in data]
    val = 14
    while True:
        temp = items[:14]
        ret = True
        for i in temp:
            if temp.count(i) != 1:
                ret = False
        if ret:
            print(val)
            return(val)
        else:
            items.pop(0)
            val+=1
