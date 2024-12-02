with open("./aoc/2024/day 02/data.txt") as f:
    data = f.read().split("\n")


def check(numbers):
    increasing = numbers[0] < numbers[1]
    for n in range(len(numbers)-1):
        if (numbers[n] < numbers[n+1]) != increasing or numbers[n] == numbers[n+1] or abs(numbers[n+1]-numbers[n]) > 3:
            return False
    return True


total = 0
for line in data:
    numbers = [int(x) for x in line.split(" ")]
    for n in range(len(numbers)):
        if check(numbers[:n] + numbers[n+1:]):
            total += 1
            break

        
    
print(total)
