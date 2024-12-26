with open("./aoc/2024/day 21/data.txt") as f:
    data = f.read().split("\n")

print(data)

"""
789
456
123
 0A


 ^A
<v>


keypad by me -> keypad by robot -> keypad by robot -> numberpad by robot
"""

numberpad = {
}
lengths = {}

directions = ((1,0,"v"),(-1,0,"^"),(0,1,">"),(0,-1,"<"))
#bfs to get everything in relation to each other
n = "789\n456\n123\n 0A".split("\n")
for y in range(4):
    for x in range(3):
        if y==3 and x==0:
            continue 

        
        key = n[y][x]
        numberpad[key] = {key:["A"]}
        lengths[key] = {key:1} 
        queue = [(y,x,"")]
        while queue != []:
            newq = []
            # print("key",key,"already",alreadyThere,"q",queue)
            for y1,x1,path in queue:
                for dy,dx,code in directions:
                    if y1+dy>=0 and y1+dy<4 and x1+dx>=0 and x1+dx<3:
                        newkey = n[y1+dy][x1+dx]

                        if newkey == " ":
                            continue


                        if newkey not in numberpad[key]:
                            lengths[key][newkey] = len(path) + 2
                            numberpad[key][newkey] = []
                        if len(path) + 2 > lengths[key][newkey]:
                            continue

                        numberpad[key][newkey].append(path+code+"A")
                        newq.append((y1+dy,x1+dx,path+code))

            queue = newq.copy()

n2 = " ^A\n<v>".split("\n")
lengths2={}
keypad = {
}
for y in range(2):
    for x in range(3):
        if y==0 and x==0:
            continue 

        
        key = n2[y][x]
        keypad[key] = {key:["A"]}
        lengths2[key] = {key:1} 
        queue = [(y,x,"")]
        while queue != []:
            newq = []
            # print("key",key,"already",alreadyThere,"q",queue)
            for y1,x1,path in queue:
                for dy,dx,code in directions:
                    if y1+dy>=0 and y1+dy<2 and x1+dx>=0 and x1+dx<3:
                        newkey = n2[y1+dy][x1+dx]

                        if newkey == " ":
                            continue


                        if newkey not in keypad[key]:
                            lengths2[key][newkey] = len(path) + 2
                            keypad[key][newkey] = []
                        if len(path) + 2 > lengths2[key][newkey]:
                            continue

                        keypad[key][newkey].append(path+code+"A")
                        newq.append((y1+dy,x1+dx,path+code))

            queue = newq.copy()



print(keypad)
# print(numberpad["A"]["0"][0] + numberpad["0"]["2"][0] + numberpad["2"]["9"][0] +numberpad["9"]["A"][0])
# idx = 0
# code = data[0]
# code1=numberpad["A"][code[0]][idx]

# for i in range(len(code) - 1):
#     code1 += numberpad[code[i]][code[i+1]][idx]
# print(code1)

# code2= keypad["A"][code1[0]][idx]

# idx=0
# for i in range(len(code1) - 1):
#     code2 += keypad[code1[i]][code1[i+1]][idx]

# code3= keypad["A"][code2[0]][idx]

# idx=0
# for i in range(len(code2) - 1):
#     code3 += keypad[code2[i]][code2[i+1]][idx]

def dive(code,path,i):
    # if path == "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A":
    #     print("huzzah")
    if code == "A":
        if len(path) < leastl[0]:
            leastl[0] = len(path)
        elif len(path) > leastl[0]:
            return

        shortCodes[i].append(path)
        return #path
    if len(path) > leastl[0]:
        return #bad
    for newp in pad[code[0]][code[1]]:
        dive(code[1:], path + newp, i)

total = 0
for code in data:
    shortCodes = [[],[],[]]
    leastl=[1e10]
    #pathfind the shortest codes
    pad = numberpad.copy()

    c = "A"+code
    dive(c, "" , 0)

    pad = keypad.copy()
    leastl = [1e10]

    for c in shortCodes[0]:
        dive("A"+c, "" , 1)
    temp = []
    for c in shortCodes[1]:
        if len(c) <= leastl[0]:
            temp.append(c)
    # print(len(temp),len(shortCodes[1]))
    shortCodes[1] = temp
    
    leastl = [1e10]
    for c in shortCodes[1]:
        dive("A"+c, "" , 2)
    temp = []

    small = 1e10
    for c in shortCodes[2]:
        if len(c) < small:
            small = len(c)
        if len(c) <= leastl[0]:
            temp.append(c)
    # print(len(temp),len(shortCodes[2]))
    shortCodes[2] = temp
    
    # print(shortCodes[2])
    total += small * int(code[:-1])
    print(total)

#236932 too high
