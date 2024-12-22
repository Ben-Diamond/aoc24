with open("./aoc/2024/day 22/data.txt") as f:
    data = f.read().split("\n")


#this is way way different to what i thought it would be

done = {}
def xor(n1,n2):
    return ("1","0")[n1==n2]

def stage(a1,a2):
    out=""
    for i in range(24):
        out+= xor(a1[i],a2[i])
    return out

total=0

changes = {}
for l in range(len(data)):
    
    line = int(data[l])
    changesDone = set()
    digits = [line%10]
    lastDigit = line%10
    a = "" 
    for i in range(24):
        if line >= 2**(23-i):
            line -= 2**(23-i)
            a+="1"
        else:
            a+="0"

    x = 0
    prices={}
    while True:

        a = stage(a,a[6:]+"000000")
        a = stage(a,"00000"+a[:19])
        a = stage(a,a[11:]+"00000000000")

        x+=1

        digit = int(a,2)%10
        digits.append(digit)
        # print(digits)
        if x>=4:
            change = tuple(digits[-x]-digits[-x-1] for x in range(4,0,-1))
            #wrong
            if change not in changesDone:
                changesDone.add(change)
                if change not in changes:
                    changes[change] = 0
                changes[change] += digit


        if x==2000:
            break
    if l%100==0:
        print(l,len(changes))

    total+=int(a,2)

highest = (-1,None)
for c in changes:
    if changes[c] > highest[0]:
        highest = (changes[c],c)
print(highest) #only one minute lol