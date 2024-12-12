with open("./aoc/2024/day 11/data.txt") as f:
    rocks = [int(x) for x in f.read().split(" ")]
print(rocks)




for time in range(25):
    newRocks = []
    for rock in rocks:
        length = len(str(rock))
        if rock == 0:
            newRocks.append(1)
        elif length % 2 == 0:
            newRocks.append(int(str(rock)[:length//2]))
            newRocks.append(int(str(rock)[length//2:]))
        else:
            newRocks.append(2024*rock)
    rocks = newRocks.copy()
    # print(rocks)
    print(len(rocks))
