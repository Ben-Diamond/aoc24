with open("./aoc/2024/day 07/data.txt") as f:
    data = f.read().split("\n")





total = 0
for line in data:
    target = int(line.split(":")[0])
    numbers = [int(x) for x in line.split(":")[1].split(" ")[1:]]

    flag = False
    paths = {"": numbers[0] }
    while paths != {}:
        newPaths = {}
        for path in paths:
            if len(path) == len(numbers) - 2:
                if paths[path] + numbers[-1] == target or paths[path] * numbers[-1] == target or int(str(paths[path]) +  str(numbers[-1])) == target:
                    flag = True
                    break
                else:
                    continue
            else:
                if paths[path] > target:
                    continue
                newPaths[path+"+"] = paths[path] + numbers[len(path) + 1]
                newPaths[path+"*"] = paths[path] * numbers[len(path) + 1]
                newPaths[path+"|"] = int(str(paths[path]) +  str(numbers[len(path) + 1]))



        paths = newPaths.copy()
    if flag:
        total += target

print(total)