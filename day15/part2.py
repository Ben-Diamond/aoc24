with open("./aoc/2024/day 15/data.txt") as f:
    room,instructions = f.read().split("\n\n")
room = [list(x.replace("#","##").replace(".","..").replace("O","[]")) for x in room.split("\n")]
instructions = instructions.replace("\n","")
print(room)
print(instructions)
import time

for y in range(len(room)):
    for x in range(len(room[y])):
        if room[y][x] == "@":
            start = (y,x)
            room[y][x] = "."
            room[y].insert(x+1,".")
            break


def impose(y0,x0,direction,magnitude):
    if direction == "^":
        return y0 - magnitude,x0
    elif direction == "v":
        return y0 + magnitude,x0
    elif direction == "<":
        return y0,x0 - magnitude
    else:
        return y0, x0 + magnitude

y,x = start
print("\n".join(["".join(x) for x in room]))

def draw(room,y,x):
    out = ""
    for y2 in range(len(room)):
        if y2 != y:
            out += "".join(room[y2])
        else:
            for x2 in range(len(room[y])):
                if x2 == x:
                    out += "@"
                else:
                    out += room[y2][x2]
        out+="\n"
    with open("./aoc/2024/day 15/drawing.txt","w") as f:
        f.write(out)
    time.sleep(0.1)


for m in range(len(instructions)):
    direction = instructions[m]

    y1,x1 = impose(y,x,direction,1)
    draw(room,y,x)

    if room[y1][x1] == "#": #cannot move
        continue
    elif room[y1][x1] == ".": #simple move
        y,x = y1,x1
        continue
    elif room[y1][x1] == "[":
        #BFS here we goooo

        ends = [(y1,x1),(y1,x1+1)]
    elif room[y1][x1] == "]":
        ends = [(y1,x1-1),(y1,x1)]
    
    totalLeft,totalRight = [ends[0]],[ends[1]]
    while True:
        newEnds = []
        stop = False
        for end in ends:
            newY,newX = impose(end[0],end[1],direction,1)
            obj = room[newY][newX]
            if obj == "[": #this and the one to the right of it
                totalLeft.append((newY,newX))
                newEnds.append((newY,newX))

                if direction == "^" or direction == "v":
                    totalRight.append((newY,newX + 1))
                    newEnds.append((newY,newX+1))

            elif obj == "]": #this and the one to the left of it
                
                totalRight.append((newY,newX))
                newEnds.append((newY,newX))


                if direction == "^" or direction == "v":
                    totalLeft.append((newY,newX-1))
                    newEnds.append((newY,newX-1))
                
                
            elif obj == "#": #mission terminated
                stop = True
                break
            #if ., do nothing

        if stop:
            break #sad!
        if newEnds == []: #we can do the move!!!
            totalLeftEnd, totalRightEnd = set(),set()
            for boxY,boxX in totalLeft:
                newY,newX = impose(boxY,boxX,direction,1)
                room[newY][newX] = "["
                totalLeftEnd.add((newY,newX))
            for boxY,boxX in totalRight:
                newY,newX = impose(boxY,boxX,direction,1)
                room[newY][newX] = "]"
                totalRightEnd.add((newY,newX))
            y,x = y1,x1
            for boxY,boxX in totalLeft:
                if (boxY,boxX) not in totalLeftEnd and (boxY,boxX) not in totalRightEnd:
                    room[boxY][boxX] = "."
            for boxY,boxX in totalRight:
                if (boxY,boxX) not in totalLeftEnd and (boxY,boxX) not in totalRightEnd:
                    room[boxY][boxX] = "."

            break
        
        ends = newEnds.copy()

print("\n".join(["".join(b) for b in room]),y,x)




total = 0
for y in range(len(room)):
    for x in range(len(room[y])):
        if room[y][x] == "[":
            total += 100*y + x
print(total)