with open("./aoc/2024/day 17/data.txt") as f:
    data, instructions = f.read().split("\n\n")

data = data.split("\n")
A = int(data[0].split(": ")[1])
B = int(data[1].split(": ")[1])
C = int(data[2].split(": ")[1])

instructions = list(map(int,instructions.replace("Program: ","").split(",")))

print(instructions)

def combo(o):
    if o <= 3:
        return o
    elif o == 4:
        return A
    elif o == 5:
        return B
    elif o == 6:
        return C
    else:
        print("uhh 7 is reserved...")


def bxl(a,b):
    if a >= b:
        a = str(bin(a)).replace("b","0")
        b = str(bin(b).zfill(len(a))).replace("b","0")
    else:
        b = str(bin(b)).replace("b","0")
        a = str(bin(a).zfill(len(b))).replace("b","0")
    out = ""
    # print(a,b)
    for i in range(len(a)):
        out += "0" if a[i] == b[i] else "1"
    return int(out,2)
        
output=[]
def perform(opcode,operand,A,B,C,pointer):
    if opcode == 0:
        A = A // (2**combo(operand))
        return A,B,C,pointer + 2
    elif opcode == 1:
        B = bxl(B, operand )
        return A,B,C,pointer + 2
    elif opcode == 2:
        B = combo(operand) % 8
        return A,B,C,pointer + 2
    elif opcode == 3:
        if A != 0:
            return A,B,C,operand
        return A,B,C,pointer + 2
    elif opcode == 4:
        B = bxl(B,C)
        return A,B,C,pointer + 2
    elif opcode == 5:
        output.append(str(combo(operand)%8))
        return A,B,C,pointer + 2
    elif opcode == 6:
        B = A // (2**combo(operand))
        return A,B,C,pointer + 2
    elif opcode == 7:
        C = A // (2**combo(operand))
        return A,B,C,pointer + 2

# print(bxl(10,2))
pointer = 0

while pointer < len(instructions):
    opcode = instructions[pointer]
    operand = instructions[pointer + 1]
    A,B,C,pointer = perform(opcode,operand,A,B,C,pointer)
    print(A,B,C,pointer)
print(",".join(output))
