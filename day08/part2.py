with open("./aoc/2024/day 08/data.txt") as f:
    data = f.read().split("\n")


nodes = {}
antinodes = set()

for y,line in enumerate(data):
    for x,letter in enumerate(line):
        if letter != ".":
            if letter not in nodes:
                nodes[letter] = set()
            nodes[letter].add((x,y))

for node in nodes:
    positions = nodes[node]
    for node1 in positions:
        x1,y1 = node1
        for node2 in positions:
            if node1 == node2:
                continue
            x2,y2 = node2
            for d in range(1,10000): #forwards cause it does both anyway
                x3 = x1 + d*(x2 - x1)
                y3 = y1 + d*(y2 - y1)
                if x3 < len(data[0]) and x3 >= 0 and y3 < len(data) and y3 >= 0:
                    antinodes.add((x3,y3))
                else:
                    break

print(antinodes)
print(len(antinodes))

def draw():
    out=""
    for y in range((len(data))):
        for x in range(len(data[y])):
            if (x,y) in antinodes:
                out += "#"
            else:
                out += data[y][x]
        out += "\n"
    with open("./aoc/2024/day 08/drawing.txt","w") as f:
        f.write(out)
draw()