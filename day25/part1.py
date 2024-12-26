with open("./aoc/2024/day 25/data.txt") as f:
    data = [x.split("\n") for x in f.read().split("\n\n")]

locks = []
keys = []

for thing in data:
    heights = []
    if thing[0][0] == ".": #key
        for x in range(len(thing[0])):
            for y in range(len(thing)):
                if thing[y][x] == "#":
                    heights.append(y)
                    break
                    #not how they did it
                    #overlap if LESS
        keys.append(heights)
    else: #lock
        for x in range(len(thing[0])):
            for y in range(len(thing)):
                if thing[y][x] == ".":
                    heights.append(y)
                    break
        locks.append(heights)
print(locks)
print(keys)
 #if key is less than lock
total = 0
for lock in locks:
    for key in keys:

        flag=True
        for x in range(len(key)):
            if key[x] < lock[x]:
                flag = False
                break
        if flag:
            # print(lock,key)
            total += 1
print(total)
