with open("./aoc/2024/day 18/data.txt") as f:
    data = f.read().split("\n")

bits = set()

for l,line in enumerate(data):
    if l == 1024:
        break
    bits.add((int(line.split(",")[0]),int(line.split(",")[1])))
# print(bits)

queue = [(0,0)]
seen = set()
for t in range(1,70*70+1):
    newq = []
    
    for point in queue:
        x,y = point
        for point2 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if x < 0 or x > 70 or y < 0 or y > 70:
                continue
            if point2 == (70,70):
                print(t)
                exit()
            if point2 in bits or point2 in seen:
                continue
            newq.append(point2)
            seen.add(point2)

    queue = newq.copy()