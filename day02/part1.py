with open("./aoc/2024/day 02/data.txt") as f:
    data = f.read().split("\n")

total = 0
for line in data:
    numbers = [int(x) for x in line.split(" ")]
    increasing = numbers[0] < numbers[1]
    flag = True
    for n in range(len(numbers)-1):
        if (numbers[n] < numbers[n+1]) != increasing or numbers[n] == numbers[n+1] or abs(numbers[n+1]-numbers[n]) > 3:
            flag = False
            break
    if flag:
        total += 1
    
print(total)
