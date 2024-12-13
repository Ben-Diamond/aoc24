with open("./aoc/2024/day 13/data.txt") as f:
    data = f.read().split("\n\n")


machines = []
for block in data:
    lines = block.split("\n")
    machine = {}
    machine["A"] = (int(lines[0].split("X+")[1].split(",")[0]),int(lines[0].split("Y+")[1]))
    machine["B"] = (int(lines[1].split("X+")[1].split(",")[0]),int(lines[1].split("Y+")[1]))
    machine["P"] = (int(lines[2].split("X=")[1].split(",")[0]),int(lines[2].split("Y=")[1]))
    machines.append(machine)

total = 0
for machine in machines:
    A,B,P = machine["A"], machine["B"], machine["P"],
    aPress = round(( P[0] - P[1]*B[0]/B[1] ) / ( A[0] - A[1]*B[0]/B[1] ))
    bPress = round((P[1] - A[1]*aPress) / B[1])

    if A[0] % B[0] == 0 and A[1] % B[1] == 0:
        print(machine)
    if B[0] % A[0] == 0 and B[1] % A[1] == 0:
        print(machine)
    if A[0] / A[1] == B[0] / B[1]:
        print(machine)

    print(aPress,bPress,round(aPress),round(bPress))
    #round and check because stupid tiny errors

    if aPress >=0 and bPress >=0 and A[1]*aPress  + B[1]*bPress == P[1] and A[0]*aPress  + B[0]*bPress == P[0]:
        total += 3*aPress + bPress
print(int(total))

#24734 too LOW
"""
freaking rounding ruined it

solve simultaneously 
When they are linearly independend
94a + 22b = 8400;
34a + 67b = 5400
67b = 5400 - 34a
b = (5400 - 34a) * (1/67)
thus b = (P[1] - A[1]a) / B[1]
and substitute;
A[0]a + B[0]* ((P[1] - A[1]a) / B[1]) = P[0]
a( A[0] - A[1]B[0]/B[1] ) = P[0] - P[1]B[0]/B[1]
a = ( P[0] - P[1]B[0]/B[1] ) / ( A[0] - A[1]B[0]/B[1] )

e.g. a=2,b=3
a + 3b = 11
3a + 2b = 12
a = (11 - 12*3/2) / (1 - 3*3/2)
a = (11 - 18)  / (1 - 4.5)
a = -7 / -3/5
a = 2 (correct)

b = (12 - 3*2) / 2
b = 6 / 2
b = 3 (correct)
"""
