with open("./aoc/2024/day 06/data.txt") as f:
    data = f.read().split("\n")

walls = set()
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "#":
            walls.add((y,x))
        elif data[y][x] == "^":
            start = ((y,x))

directions = ((-1,0),(0,1),(1,0),(0,-1))

y,x = start
direction = 0
visited = {start}
while y >= 0 and x >= 0 and y < len(data) and x <len(data[0]):
    newY,newX = y + directions[direction][0], x + directions[direction][1]
    if (newY,newX) in walls:
        direction = (direction + 1) % 4
    else:
        y,x = newY,newX
        if y >= 0 and x >= 0 and y < len(data) and x <len(data[0]) and (y,x) not in visited:
            visited.add((y,x))

        

def draw():
    with open("./aoc/2024/day 06/drawing.txt","w") as f:
        out = ""
        for y in range(len(data)):
            for x in range(len(data[0])):
                if (y,x) in walls:
                    out += "X"
                elif (y,x) in visited:
                    out += "#"
                else:
                    out += "."

            out += "\n"
        f.write(out)
draw()
print(len(visited))

#4987 too low
