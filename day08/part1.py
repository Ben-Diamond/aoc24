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
            x3 = x1 + 2*(x2 - x1)
            y3 = y1 + 2*(y2 - y1)
            if x3 < len(data[0]) and x3 >= 0 and y3 < len(data) and y3 >= 0:
                antinodes.add((x3,y3))

print(antinodes)
print(len(antinodes))
