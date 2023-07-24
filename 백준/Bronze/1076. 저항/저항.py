color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
gop = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
res = []
a = 0
b = 0
for i in range(3):
    jeohang = input()
    if len(res) == 2:
        a = res[0]+res[1]
        b = color.index(jeohang)
    else :
        res.append(str(color.index(jeohang)))
c = gop[b]
print(int(a)*c)
