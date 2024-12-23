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
total = 0

for c1 in connections:
    for c2 in connections[c1]:
        for c3 in connections[c1]:
            if c2 != c3 and c3 in connections[c2] and( c1[0]=="t" or c2[0]=="t" or c3[0]=="t"):
                total+=1
                
    print(total//6)
#2364 too high
