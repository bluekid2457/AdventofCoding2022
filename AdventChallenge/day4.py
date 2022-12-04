with open("input.txt") as f:
    data = f.read()
def p1():
    items = data.split('\n')
    sum = 0
    for i in items:
        e1 = i.split(",")[0]
        e2 = i.split(',')[1]
        e1min = int(e1.split("-")[0])
        e1max = int(e1.split("-")[1])
        e2min = int(e2.split("-")[0])
        e2max = int(e2.split("-")[1])
        if e1min <= e2min and e1max >= e2max:
            sum+=1
        elif e2min <= e1min and e2max >= e1max:
            sum+=1
        
    print(sum)
def p2():
    items = data.split('\n')
    sum = 0
    for i in items:
        e1 = i.split(",")[0]
        e2 = i.split(',')[1]
        e1min = int(e1.split("-")[0])
        e1max = int(e1.split("-")[1])
        e2min = int(e2.split("-")[0])
        e2max = int(e2.split("-")[1])
        add = True
        for i in range(e2min,e2max+1):
            if i in range(e1min,e1max+1):
                add = False
        if not(add):
            sum+=1
    print(sum,"answer")