with open("./aoc/2024/day 01/data.txt") as f:
    data = f.read().split("\n")

def insertion(num,array):
    i = 0
    while True:
        if i == len(array):
            break
        if num > array[i]:
            i += 1
        else:
            break
    array.insert(i,num)

left, right = [],[]

for line in data:
    num1 = int(line.split(" ")[0])
    insertion(num1,left)
    
    num2 = int(line.split(" ")[-1])
    insertion(num2,right)

total = 0
for x in range(len(left)):
    total += abs(left[x]-right[x])

print(total)