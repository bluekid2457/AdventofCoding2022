with open("input.txt") as f:
    data = f.read()
data = (data.split('\n\n'))
for c,i in enumerate(data):
    val = i.split('\n')
    val = [int(k) for k in val]
    val = sum(val)
    data[c] = val
print(data)
e1 = max(data)
data.remove(e1)

e2 = max(data)
data.remove(e2)

e3 = max(data)
data.remove(e3)
print(max(data))
print(e1,e2,e3)
print(e1+e2+e3)
max = 0
#for elf in data:
    