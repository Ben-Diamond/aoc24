with open("./aoc/2024/day 09/data.txt") as f:
    data = f.read()


blocks = []
#2 : 3, 5 : 1
#memory location: data left

def sumN(start,length):
    return int(((start+length-1)/2)*(start+length) - ((start-1)/2)*(start))

total = 0
location = 0
locations = []

for i in range(len(data)):
    size = int(data[i])
    if i%2 == 0:
        total += (i//2)*sumN(location,size)
    else:
        blocks.append([i,location,size])
    locations.append(location)
    location += size
    

print(blocks)
blockNumber = 0
i = len(data) - 1

for i in range(len(data)-1,-1,-2):
    for blockNumber in range(len(blocks)):
        size = int(data[i])
        blockPosition, blockLocation,blockSize = blocks[blockNumber]
        if blockPosition >= i:
            break
        if blockSize >= size:
            # print(blockNumber,i//2)
            total -= (i//2)*sumN(locations[i],size)
            total += (i//2)*sumN(blockLocation,size)
            blocks[blockNumber][2] -= size
            blocks[blockNumber][1] += size
            data = data[:i] + "0" + data[i+1:]
            break


print(blocks)

print(total)
out = ""
for i in range(len(data)):
    if i%2 == 0:
        out += data[i]
    else:
        out += str(blocks[i//2][2])
# print(out)
# print(data)

#6430446956401 too high