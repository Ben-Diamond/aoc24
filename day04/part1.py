with open("./aoc/2024/day 04/data.txt") as f:
    data = f.read().split("\n")

locations = {
    "X":set(),
    "M":set(),
    "A":set(),
    "S":set()
}



for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] in locations:
            locations[data[y][x]].add((x,y))

#across, down

def impose(a,b,bScale):
    return (a[0]+b[0]*bScale,a[1]+b[1]*bScale)

directions = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1))

total = 0
#if an A is diagonal to an M, there must be an S after it, and one of each A and M on the other corners
for wordStart in locations["X"]:
    for dir in directions:
        if impose(wordStart,dir,1) in locations["M"]:
            if impose(wordStart,dir,2) in locations["A"]:
                if impose(wordStart,dir,3) in locations["S"]:
                    total += 1
print(total)
