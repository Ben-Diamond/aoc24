with open("./aoc/2024/day 23/data.txt") as f:
    data = f.read().split("\n")

connections = {}
for line in data:
    a,b = line[:2],line[3:]
    if a not in connections:
        connections[a] = set()
    connections[a].add(b)
    if b not in connections:
        connections[b] = set()
    connections[b].add(a)
print(connections)
b = 0
groups = set()
tried=set()

#everything is connected only to thirteen things


def dive(computers):

    if tuple(sorted(computers)) in tried:
        return len(computers)
    
    biggest=len(computers)
    if biggest == 13:
        print(",".join(sorted(computers)))
    for c in connections[computers[0]]:
        if c in computers:
            continue
        flag=True
        for d in computers[1:]:
            if c not in connections[d]:
                flag=False
        if flag:
            temp = dive(computers+[c])
            if temp > biggest:
                biggest = temp
    # print(computers)
    tried.add(tuple(sorted(computers)))
    return biggest
#it is NOT twelve

for e in connections:

    temp=dive([e])
    #just to global nonsense next time
    if temp>b:
        b=temp
        print("!!!!!!",b)