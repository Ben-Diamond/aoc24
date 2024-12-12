with open("./aoc/2024/day 11/data.txt") as f:
    data = [int(x) for x in f.read().split(" ")]
print(data)

rocks = {}
for rock in data:
    rocks[rock] = data.count(rock)

prev = set()
total = 0
for time in range(75):
    newRocks = {}
    for rock in rocks:
        # if rock in prev:
        #     total += 1
        # prev.add(rock)
        length = len(str(rock))
        if rock == 0:
            if 1 not in newRocks:
                newRocks[1] = 0
            newRocks[1] += rocks[rock]
        elif length % 2 == 0:
            for r in (int(str(rock)[:length//2]),int(str(rock)[length//2:])):
                if r not in newRocks:
                    newRocks[r] = 0
                newRocks[r] += rocks[rock]
        else:
            if 2024*rock not in newRocks:
                newRocks[2024*rock] = 0
            newRocks[2024*rock] += rocks[rock]
    rocks = newRocks.copy()
    # print(rocks)

for rock in rocks:
    total += rocks[rock]
print(total)