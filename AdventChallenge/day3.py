import re
def Convert(string):
    return re.findall('[a-zA-Z]', string)
with open("input.txt") as f:
    data = f.read()

def IOfSets(arr1, arr2, arr3):
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
    set1 = s1.intersection(s2)   
    rset = set1.intersection(s3)
    final = list(rset)
    return(final[0])

def finder(list1, list2, list3):
  return list(set(list1).intersection(list2, list3))
data = data.split('\n')
def p2():
    n = []
    while len(data) !=0:
        try:
            n.append([data[0],data[1],data[2]])
            data.pop(0)
            data.pop(0)
            data.pop(0)
        except:
            print(data,len(data))
    ret = []
    for i in n:
        k = IOfSets(Convert(i[0]),Convert(i[1]),Convert(i[2]))
        ret.append(k)
    s = 0
    for i in ret:
        if i == None:
            pass
        elif i.isupper():
            s+=ord(i)-64+26
        elif i.islower():
            s+=ord(i)-96
        else:
            print("BAADDD")
    print(s)

def p1():
    l1 = [i[:len(i)//2] for i in data]
    #print(l1)
    l2 = [i[(len(i)//2):] for i in data]
    #print(l2[0])

    ret = []
    for c,i in enumerate(l1):
        ret2 = set()
        for k in i:
            if k in l2[c]:
                ret2.add(k)
        for i in ret2:
            ret.append(i)
    sum = 0
    for i in ret:
        if i.isupper():
            sum+=ord(i)-64+26
        elif i.islower():
            sum+=ord(i)-96
        else:
            print("BAADDD")
    print(sum)
print(finder([0,2,3],[0,5,6,3],[9,3,0,4,5]))