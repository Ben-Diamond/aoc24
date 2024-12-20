with open("./aoc/2024/day 20/data.txt") as f:
    data = f.read().split("\n")

distances = {}
cheats = {}

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            start = (x,y)
        elif data[y][x] == "E":
            end = (x,y)

#BFS to get how far all the points are
#then for skips see if the difference is big enough


#oh goodness it's now at most 20...
queue = [end]

for time in range(100000):
    newq = []
    for x,y in queue:
        # print(x,y)
        distances[(x,y)] = time
        for x1,y1 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            #line of # around means we do not need to check bounds
            if (data[y1][x1] == "." or data[y1][x1] == "S") and (x1,y1) not in distances:
                distances[(x1,y1)] = -1
                newq.append((x1,y1))

    queue = newq.copy()
    # break
    if queue == []:
        break

print(distances[start])

for node in distances:
    x,y = node
    #find all DOTS everything in a 20 manhattan distance
    for dy in range(-20,21):
        if dy >=0:
            lb,ub = dy-20,21-dy
        else:
            lb,ub = -20-dy,dy+21
        for dx in range(lb,ub):
            newp = (x+dx,y+dy)
            if newp in distances and distances[node] - distances[newp] > abs(dx) + abs(dy):
                cheats[(x,y,x+dx,y+dy)] = distances[node] - distances[newp] - abs(dx) - abs(dy)

total = 0
for c in cheats:
    if cheats[c] >= 100:
        total += 1
print(total)