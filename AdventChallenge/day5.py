with open("input.txt") as f:
    data = f.read()
def unraveldata(): #failed attempt to not hardcode crates
    print(data)
    items = data.split('\n')
    for i in items:
        for k in range(1,18,2):
            if i[k] != " ":
                print(i[k],end = " -- ")

def move(istack,fstack,num):
    global fullstack
    #print(istack,"from")
    for i in range(num):
        item = fullstack[istack-1][-1]
        fullstack[fstack-1].append(item)
        fullstack[istack-1].pop(-1)

def move2(istack,fstack,num):
    global fullstack
    #print(istack,"from")
    item = fullstack[istack-1][0-num:]
    for i in item:
        fullstack[fstack-1].append(i)
    for i in range(num):
        fullstack[istack-1].pop(-1)

def p1():
    global fullstack
    
    items = data.split('\n')
    s1 = ["G",'T','R','W']
    s2 = ['G','C','H','P','M','S','V','w']
    s3 = ['C','L','T','S','G','M']
    s4 = ['J','H','D','M','W','R','F']
    s5 = ['P','Q','L','H','S','W','F','J']
    s6 = ['P','J','D','N','F','M','S']
    s7 = ['Z','B','D','F','G','C','S','J']
    s8 = ['R','T','B']
    s9 = ['H','N','W','L','C']
    fullstack = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
    stemp = []
    for i in items:
        lis = i.split(" ")
        num = int(lis[1])
        istack = int(lis[3])
        fstack = int(lis[5])
        print(f"moving{num} from{istack} to {fstack}")
        move(istack,fstack,num)
    for i in fullstack:
        print(i)
def p2():
    global fullstack
    
    items = data.split('\n')
    s1 = ["G",'T','R','W']
    s2 = ['G','C','H','P','M','S','V','w']
    s3 = ['C','L','T','S','G','M']
    s4 = ['J','H','D','M','W','R','F']
    s5 = ['P','Q','L','H','S','W','F','J']
    s6 = ['P','J','D','N','F','M','S']
    s7 = ['Z','B','D','F','G','C','S','J']
    s8 = ['R','T','B']
    s9 = ['H','N','W','L','C']
    fullstack = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
    stemp = []
    for i in items:
        lis = i.split(" ")
        num = int(lis[1])
        istack = int(lis[3])
        fstack = int(lis[5])
        print(f"moving{num} from{istack} to {fstack}")
        move2(istack,fstack,num)
    for i in fullstack:
        print(i)