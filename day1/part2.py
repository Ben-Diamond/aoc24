with open("./aoc/2024/day 01/data.txt") as f:
    data = f.read().split("\n")

right = {}
for line in data:
    num = int(line.split(" ")[-1])
    if num not in right:
        right[num] = 0
    right[num] += 1

total = 0 

for line in data:
    num = int(line.split(" ")[0])
    if num in right:
        total += num * right[num]

print(total)