with open("./aoc/2024/day 14/data.txt") as f:
    data = [x.split(" v=") for x in f.read()[2:].split("\np=")]

width = 101
height = 103
quadrants = [0,0,0,0]

for line in data:
    x0,y0 = map(int,line[0].split(","))
    vx,vy = map(int,line[1].split(","))
    
    x1,y1 = (x0 + 100*vx)%width,(y0 + 100*vy)%height
    
    if x1 == width // 2 or y1 == height // 2:
        continue
    if x1 < width // 2:
        if y1 < height // 2:
            quadrants[0] += 1
        else:
            quadrants[2] += 1
    else:
        if y1 < height // 2:
            quadrants[1] += 1
        else:
            quadrants[3] += 1
    

print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])
print(quadrants)
