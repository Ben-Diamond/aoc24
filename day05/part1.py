with open("./aoc/2024/day 05/data.txt") as f:
    data = f.read().split("\n")

befores = {}
flag1 = False
total = 0
for line in data:

    if flag1:
        works = True
        numbers = [int(x) for x in line.split(",")]
        for n in range(len(numbers)):
            for n2 in range(n+1,len(numbers)):
                if numbers[n2] in befores and numbers[n] in befores[numbers[n2]]:
                    #wrong order
                    works = False
                    break
            if not works:
                break
        if works:
            total += numbers[len(numbers)//2]
    else:   

        if line == "":
            flag1 = True
            continue
        num1,num2 = int(line.split("|")[0]),int(line.split("|")[1])
        if num1 not in befores:
            befores[num1] = set()
        befores[num1].add(num2) #num1 is BEFORE num2

print(total)

#5690 is too high