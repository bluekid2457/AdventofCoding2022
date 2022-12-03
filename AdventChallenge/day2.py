
with open("input.txt") as f:
    data = f.read()
def checkwin(oc,mc):
    if ((oc == "A" and mc == "X") or (oc == "B" and mc == "Y") or (oc == "C" and mc == "Z")):
        return(3)
    elif ((oc == "A" and mc == "Y") or (oc == "B" and mc == "Z") or (oc == "C" and mc == "X")):
        return(6)
    elif ((mc == "X" and oc == "B") or (mc == "Y" and oc == "C") or (mc == "Z" and oc == "A")):
        return(0)
    else:
        print("ERRORR")
        print(mc,oc)
def checkmove(oc,mc):
    if ((oc =="A" and mc =="Y") or (oc =="B" and mc =="X") or (oc =="C" and mc =="Z")):
        return(1)
    elif ((oc =="B" and mc =="Y") or (oc =="A" and mc =="Z") or (oc =="C" and mc =="X")):
        return(2)
    elif ((oc =="C" and mc =="Y") or (oc =="A" and mc =="X") or (oc =="B" and mc =="Z")):
        return(3)
    else:
        print("WRong")
data = data.split('\n')
#print(data)
score = 0
for i in data:
    oc = i[0]
    mc = i[2]
    score+=checkmove(oc,mc)
    if mc == "X":
        score+=0
    elif mc == "Y":
        score+=3
    elif mc == "Z":
        score+=6
    else:
        print("WOMSETHIGN WRONG")
print(score)