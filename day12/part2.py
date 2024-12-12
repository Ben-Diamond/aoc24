with open("./aoc/2024/day 12/data.txt") as f:
    data = f.read().split("\n")


#two walls can be on the same tile so long as one of them is up and one of them is across
#go through each region, check each wall
#if that wall is another tile or already in the set of walls of that orientation then ignore
#orientation = vertical or horizontal, aka above or to the side
#use pathfind to get all things in the region

def check(x,y,plantType):
    if (x,y) not in visited and x>=0 and x<len(data[0]) and y>=0 and y<len(data) and data[y][x] == plantType:
        return True
    return False

def checkPerimeter(x,y,orientation,walls,region):
    if (x,y) not in region and (x,y) not in walls[orientation]:
        return True
    return False


regions = {}
visited = set()

for y in range(len(data)):
    for x in range(len(data[y])):
        if (x,y) in visited:
            continue

        plantType = data[y][x]
        if plantType not in regions:
            
            regions[plantType] = []
        
        
        #now do bfs to find the region
        plants = [(x,y)]
        region = set()
        region.add((x,y))
        
        while plants != []:
            nextPlants = []

            for plant in plants:
                for newX,newY in (
                    (plant[0]+1,plant[1]),
                    (plant[0]-1,plant[1]),
                    (plant[0],plant[1]+1),
                    (plant[0],plant[1]-1)
                    ):
                    if check(newX,newY,plantType):
                        nextPlants.append((newX,newY))
                        region.add((newX,newY))
                        visited.add((newX,newY))

            visited.add((x,y))

            plants = nextPlants.copy()

        regions[plantType].append(region)

#FINALLY we have them nicely organised

def move(x,y,direction,magnitude):
    #if direction 0 or 1,  wall is NEXT to plant so move up-down
    return (
        (x,y+magnitude),
        (x,y+magnitude),
        (x+magnitude,y),
        (x+magnitude,y)
            )[direction]


total = 0
for letter in regions:
    for region in regions[letter]:


        walls = [set(),set(),set(),set()]
        for plant in region:
            x,y = plant
            for x1,y1,orientation in ((x+1,y,0),
                                      (x-1,y,1),
                                      (x,y+1,2),
                                      (x,y-1,3),
                                      ):
                if checkPerimeter(x1,y1,orientation,walls,region):
                    walls[orientation].add((x1,y1))
        #now group them together

        for direction in range(4): #walls2: walls in the same direction
            #if the wall is not visited, scan up and down for walls in its direction
            wallsUsed = set()
            numberFences = 0

            for wall in walls[direction]:
                x,y = wall
                if (x,y) in wallsUsed:
                    continue
                numberFences += 1
                i = 0
                while True:
                    
                    x1,y1 = move(x,y,direction,i)
                    if (x1,y1) not in wallsUsed and (x1,y1) in walls[direction]:
                        i+=1
                        wallsUsed.add((x1,y1))
                    else:
                        break
                
                i = -1
                while True:
                    x1,y1 = move(x,y,direction,i)
                    if (x1,y1) not in wallsUsed and (x1,y1) in walls[direction]:
                        i-=1
                        wallsUsed.add((x1,y1))
                    else:
                        break
            total += numberFences * len(region)
print(total)