with open("./aoc/2024/day 16/data.txt") as f:
    maze = f.read().split("\n")


#three dimensional maze - x,y,d

junctions = {}

for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == "S":
            start = (x,y,0)
            junctions[(x,y,0)] = 0
            for d in range(1,4):
                junctions[(x,y,d)] = 1e10
        elif maze[y][x] == "." and sum(
            [maze[y1][x1] == "." for y1,x1 in 
             ((y+1,x),(y-1,x),(y,x+1),(y,x-1))]
        ) > 2:
            for d in range(4):
                junctions[(x,y,d)] = 1e10

        elif maze[y][x] == "." and sum(
            [maze[y1][x1] == "." for y1,x1 in 
             ((y+1,x),(y-1,x),(y,x+1),(y,x-1))]
        ) == 2 and maze[y+1][x] != maze[y-1][x]:
            for d in range(4):
                junctions[(x,y,d)] = 1e10
        elif maze[y][x] == "E":
            end = (x,y)
            for d in range(4):
                junctions[(x,y,d)] = 1e10
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

def enqueue(node,distance):
    i=0
    while i<len(queue):

        if distance >= junctions[queue[i]]:
            i+=1
        else:
            break
    queue.insert(i,node)

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
        elif maze[y1][x1] == "E":
            print("woah")
            print(junctions[node] + i)
            exit()
        newn = (x1,y1,d)
        if newn in junctions:
            distance = junctions[node] + i
            if newn not in explored and distance < junctions[newn]:
                junctions[newn] = distance
                enqueue(newn, distance)
            
            break
    for newn in (x,y,(d+1)%4),(x,y,(d-1)%4):
        if newn in junctions:
            # print("chungus")
            distance = junctions[node] + 1000
            if newn not in explored and distance < junctions[newn]:
                
                junctions[newn] = distance
                enqueue(newn, distance)

    explored.add(node)
