with open("./aoc/2024/day 03/data.txt") as f:
    data = f.read()

total = 0
mulStart = -1
hasComma = False
digits = {"0","1","2","3","4","5","6","7","8","9"}
l = 0
while l < len(data) - 1:
    if l < len(data)-4 and data[l:l+4] == "mul(":
        l+=4
        mulStart = l
        hasComma = False
        

    if mulStart != -1:
        if data[l] == ",":
            # print(hasComma)
            if hasComma:
                mulStart = -1
            else:
                hasComma = True
        elif data[l] == ")":
            # print(hasComma)
            if not hasComma:
                mulStart = -1
            else: 
                #do
                total += (int(data[mulStart:l].split(",")[0]))*(int(data[mulStart:l].split(",")[1]))
                mulStart = -1
        elif data[l] not in digits:
            # print(data[l])
            mulStart = -1
    
    l += 1
print(total)
