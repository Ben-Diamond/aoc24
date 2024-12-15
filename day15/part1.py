with open("./aoc/2024/day 15/data.txt") as f:
    room,instructions = f.read().split("\n\n")
room = [list(x) for x in room.split("\n")]
instructions = instructions.replace("\n","")
print(room)
print(instructions)

for y in range(len(room)):
    for x in range(len(room[y])):
        if room[y][x] == "@":
            start = (y,x)
            room[y][x] = "."
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
import time
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
    with open("./aoc/2024/day 15/drawing1.txt","w") as f:
        f.write(out)
    time.sleep(0.01)

for m in range(len(instructions)):
    direction = instructions[m]

    y1,x1 = impose(y,x,direction,1)
    # print("\n".join(["".join(b) for b in room]),y,x)
    draw(room,y,x)

    if room[y1][x1] == "#": #cannot move
        continue
    elif room[y1][x1] == ".": #simple move
        y,x = y1,x1
    elif room[y1][x1] == "O": #find the end of the line of boxes
        boxY,boxX = y1,x1
        while room[boxY][boxX] == "O":
            boxY,boxX = impose(boxY,boxX,direction,1)
        #now it's the first non box
        if room[boxY][boxX] == "#": #cannot move
            continue
        elif room[boxY][boxX] == ".":
            room[y1][x1] = "."
            room[boxY][boxX] = "O"
            y,x = y1,x1
        else:
            print("boxs ????")
    else:
        print("??????????")


total = 0
for y in range(len(room)):
    for x in range(len(room[y])):
        if room[y][x] == "O":
            total += 100*y + x
print(total)
