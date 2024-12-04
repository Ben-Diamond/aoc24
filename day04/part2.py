with open("./aoc/2024/day 04/data.txt") as f:
    data = f.read().split("\n")

locations = {
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
def impose2(a,b,bScale):
    return (a[0]+b[0]*-bScale,a[1]+b[1]*bScale)

directions = ((1,1),(1,-1),(-1,-1),(-1,1))

total = 0
#if an M is diagonal to an A, there must be an S opposite, and another such pair (many such cases)
for wordStart in locations["A"]:
    for dir in directions:
        if impose(wordStart,dir,1) in locations["M"]:
            if impose(wordStart,dir,-1) in locations["S"]:
                if ((impose2(wordStart,dir,1) in locations["M"] and impose2(wordStart,dir,-1) in locations["S"])
                or (impose2(wordStart,dir,-1) in locations["M"] and impose2(wordStart,dir,1) in locations["S"])):
                    total += 0.5 #le troll
print(int(total))