with open("./aoc/2024/day 22/data.txt") as f:
    data = f.read().split("\n")


done = {}
def xor(n1,n2):
    return ("1","0")[n1==n2]

def stage(a1,a2):
    out=""
    for i in range(24):
        out+= xor(a1[i],a2[i])
    return out

total=0
t=0
for l in range(len(data)):
    line = int(data[l])

    a = "" 
    for i in range(24):
        if line >= 2**(23-i):
            line -= 2**(23-i)
            a+="1"
        else:
            a+="0"
    o=a
    x = 0
    
    while True:
        a = stage(a,a[6:]+"000000")
        a = stage(a,"00000"+a[:19])
        a = stage(a,a[11:]+"00000000000")

        x+=1
        if x==2000:
            break
    # print(l)
    # print(a,int(a,2))
    if l%100 == 0:
        print(l)

    # print(done)
    total+=int(a,2)
#20407339931 too high
print(total)

