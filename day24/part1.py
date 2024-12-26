with open("./aoc/2024/day 24/data.txt") as f:
    data = [x.split("\n") for x in f.read().split("\n\n")]

wires = {}
gates = []

operators = {
    "XOR": lambda x, y: (1, 0)[x == y],
    "AND": lambda x, y: (0,1)[x and y],
    "OR": lambda x, y: (0,1)[x or y],

}

for line in data[0]:
    wires[line.split(":")[0]] = int(line.split(":")[1])
for line in data[1]:
    line = line.split(" ")
    gates.append((line[0],line[2],line[1],line[4]))
# print(gates)



while True:
    flag=False
    for gate in gates:
        if gate[0] in wires and gate[1] in wires and gate[3] not in wires:
            wires[gate[3]] = operators[gate[2]]( wires[gate[0]], wires[gate[1]] )
            flag=True
    if not flag:
        break
        
total = 0
print(total)
for x in range(1000):
    wire = "z"+("0" if x<10 else "")+str(x)
    if wire not in wires:
        print(total)
        break
    print(wire,wires[wire])
    total += wires[wire] * (2**int(wire[1:]))
