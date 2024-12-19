with open("./aoc/2024/day 19/data.txt") as f:
    data = f.read().split("\n\n")

patterns = data[0].split(", ")
designs = data[1].split("\n")
print(patterns)
print(designs)
results = {}
#dfs (somehow)

def addTowel(design):
    arrangements = 0
    if design in results:
        return results[design]
    for pattern in patterns:
        # print(design,design[:len(pattern)], "TRY",pattern)
        if pattern == design:
            # print("so true",design)
            arrangements += 1
        
        if len(pattern) >= len(design):
            continue #equal to, since we covered when they match

        if design[:len(pattern)] == pattern:
            # print("through")
            ans = addTowel(design[len(pattern):])
            if ans:
                arrangements += ans
    results[design] = arrangements
    return arrangements
total = 0
for d in designs:
    total += addTowel(d)
print(total)

# print(len(results))