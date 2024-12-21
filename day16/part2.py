with open("./aoc/2024/day 16/data.txt") as f:
    maze = f.read().split("\n")


#three dimensional maze - x,y,d

junctions = {}
prevs = {}

for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == "S":
            start = (x,y,0)
            junctions[(x,y,0)] = 0
            prevs[(x,y,0)] = []
            for d in range(1,4):
                junctions[(x,y,d)] = 1e10
                prevs[(x,y,d)] = []
        elif maze[y][x] == "." and sum(
            [maze[y1][x1] == "." for y1,x1 in 
             ((y+1,x),(y-1,x),(y,x+1),(y,x-1))]
        ) > 2:
            for d in range(4):
                junctions[(x,y,d)] = 1e10
                prevs[(x,y,d)] = []

        elif maze[y][x] == "." and sum(
            [maze[y1][x1] == "." for y1,x1 in 
             ((y+1,x),(y-1,x),(y,x+1),(y,x-1))]
        ) == 2 and maze[y+1][x] != maze[y-1][x]:
            for d in range(4):
                junctions[(x,y,d)] = 1e10
                prevs[(x,y,d)] = []
        elif maze[y][x] == "E":
            end = (x,y)
            for d in range(4):
                junctions[(x,y,d)] = 1e10
                prevs[(x,y,d)] = []
            ends = ((x,y,0),(x,y,1),(x,y,2),(x,y,3))
#dijkstra's shortest path

def move(x,y,direction,mag):
    if direction == 0:
        return x+mag,y
    elif direction == 1:
        return x,y+mag
    elif direction == 2:
        return x-mag,y
    else:
        return x,y-mag
    
def rotate(node,number):
    return (node[0],node[1],(node[2]+number)%4)

weights = (
    (0,1000,2000,1000),
    (1000,0,1000,2000),
    (2000,1000,0,1000),
    (1000,2000,1000,0),
)

def enqueue(node,distance):
    # print(node,distance)
    # nextQueue.append(node)
    i=0
    while i<len(queue):

        if distance >= junctions[queue[i]]:
            i+=1
        else:
            break
    queue.insert(i,node)

def fixprevs(node,prev,equal):
    if not equal:
        prevs[node] = [prev]
    else:
        prevs[node].append(prev)


explored = set()

queue = [(start)]


while queue != []:
    node = queue.pop(0)
    #explore all from this 
    x,y,d = node
    for i in range(1,1000): #attempt to move forwards
        x1,y1 = move(x,y,d,i)
        if maze[y1][x1] == "#":
            break #sad!
        # elif maze[y1][x1] == "E":
        #     print("woah")
        #     print(junctions[node] + i)
        #     exit()
        newn = (x1,y1,d)
        if newn in junctions:
            distance = junctions[node] + i
            if newn not in explored and distance <= junctions[newn]:
                fixprevs(newn,node,distance==junctions[newn])
                junctions[newn] = distance
                enqueue(newn, distance)
            
            break
    
    # newn = (x,y,(d+1)%4)
    for newn in (x,y,(d+1)%4),(x,y,(d-1)%4):
        if newn in junctions:
            # print("chungus")
            distance = junctions[node] + 1000
            if newn not in explored and distance < junctions[newn]:
                fixprevs(newn,node,distance==junctions[newn])
                junctions[newn] = distance
                enqueue(newn, distance)
    explored.add(node)
    if (end[0],end[1],3) in explored:
        break
routesUsed = set()
#dfs too slow
def dive(node):
    if node == start:
        # print("wowie zowie")
        # print(routesUsed,len(routesUsed))
        return
    for prev in prevs[node]:
        if (prev[0],prev[1]) != (node[0],node[1]):
            routesUsed.add((
                node[0],node[1],prev[0],prev[1]
            ))
        dive(prev)
print("...")

queue = {(end[0],end[1],3)}
spaces=set()
total = 0
out = [list(x)for x in maze.copy()]

while True:
    newq = set()
    # print(len(queue))
    for node in queue:
        if node == start:
            continue
        for prev in prevs[node]:
            x1,y1,x2,y2 = node[0],node[1],prev[0],prev[1]    
            if x1 < x2:
                for x3 in range(x1,x2+1):
                    out[y1][x3] = "O"    
                    spaces.add((x3,y1))        
            elif x1 > x2:
                for x3 in range(x2,x1+1):
                    out[y1][x3] = "O"
                    spaces.add((x3,y1))    
            elif y1 < y2:
                for y3 in range(y1,y2+1):
                    out[y3][x1] = "O"
                    spaces.add((x1,y3))    
            else:
                for y3 in range(y2,y1+1):
                    out[y3][x1] = "O"
                    spaces.add((x1,y3))    
            # out[y1][x1] = "O"
            # out[y2][x2] = "O"
            if (x1,y1) != (x2,y2) and (x1,y1,x2,y2) not in routesUsed:
                
                routesUsed.add((x1,y1,x2,y2))
                total += abs(x1-x2) + abs(y1-y2)
            newq.add(prev)
    
    queue = newq.copy()
    if len(queue) == 0:
        break

print(len(spaces)) #total didnt work cause what if multiple paths end at the same place (?)
with open("./aoc/2024/day 16/drawing.txt","w") as f:
    f.write("\n".join(["".join(x) for x in out]))
