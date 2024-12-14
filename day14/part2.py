with open("./aoc/2024/day 14/data.txt") as f:
    data = [x.split(" v=") for x in f.read()[2:].split("\np=")]

import time
width = 101
height = 103
quadrants = [0,0,0,0]
robots = []

for line in data:
    x0,y0 = map(int,line[0].split(","))
    vx,vy = map(int,line[1].split(","))
    robots.append((x0,y0,vx,vy))

def draw(positions,t):
    out = f"\n--------------------------------------------------------------------\nt={t}\n-----------------------------------------------------\n\n"
    for y in range(height):
        for x in range(width):
            if (x,y) in positions:
                out += "#"
            else:
                out += "."
        out += "\n"
    with open("./aoc/2024/day 14/drawing.txt","a") as f:
        f.write(out)
#228
t = 0
while True:
    t += 1
    flag = False
    positions = set()
    for robot in robots:
        pos = (((robot[0] + t*robot[2])%width),((robot[1] + t*robot[3])%height))
        if pos in positions:
            flag = True
        else:
            positions.add(pos)
    if not flag:
        print(t)
        draw(positions,t)
        break
    # time.sleep(0.5)


    

print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])
print(quadrants)
