with open("./aoc/2024/day 19/data.txt") as f:
    data = f.read().split("\n\n")

patterns = data[0].split(", ")
designs = data[1].split("\n")
print(patterns)
print(designs)
results = {}
#dfs (somehow)

def addTowel(design):
    if design in results:
        return results[design]
    for pattern in patterns:
        # print(design,design[:len(pattern)], "TRY",pattern)
        if pattern == design:
            results[pattern] = True
            # print("so true",design)
            return True
        
        if len(pattern) >= len(design):
            continue #equal to, since we covered when they match

        if design[:len(pattern)] == pattern:
            # print("through")
            if addTowel(design[len(pattern):]):
                results[design[len(pattern):]] = True
                return True
            
    results[design] = False
    return False
total = 0
for d in designs:
    total += addTowel(d)
print(total)

# print(len(results))
