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

# print(distances)
print(distances[start])

#check skipping one
for node in distances:
    x,y = node
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        endpoint = (x+2*dx,y+2*dy)
        if (x+dx,y+dy) not in distances and endpoint in distances:
            if distances[node] - distances[endpoint] > 2:
                cheats[(x,y,endpoint[0],endpoint[1])] = distances[node] - distances[endpoint] - 2

total = 0
for c in cheats:
    if cheats[c] >= 100:
        total += 1
print(total)
