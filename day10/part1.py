with open("./aoc/2024/day 10/data.txt") as f:
    data = f.read().split("\n")

width,length = len(data),len(data[0])
def check(x,y,num):
    if y >= 0 and y < width and x >= 0 and x < length:
        if data[y][x] == num:
            return True
    return False

total = 0
for y0 in range(width):
    for x0 in range(length):

        if data[y0][x0] == "0":
            #ok now do it
            paths = [(x0,y0)]
            
            for time in range(1,10):
                newPaths = set()
                for x,y in paths:
                    # print(x,y)
                    for newX,newY in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                        if check(newX,newY,str(time)):
                            newPaths.add((newX,newY))
                
                paths = newPaths.copy()
            print(paths,len(paths))
            total += len(paths)
print(total)
