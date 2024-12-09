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
while blockNumber < len(blocks):
    size = int(data[i])
    blockPosition, blockLocation,blockSize = blocks[blockNumber]
    if blockPosition >= i:
        break
    if blockSize == 0:
        blockNumber += 1
    elif blockSize > size:
        total -= (i//2)*sumN(locations[i],size)
        total += (i//2)*sumN(blockLocation,size)
        blocks[blockNumber][2] -= size
        blocks[blockNumber][1] += size
        data = data[:i] + "0" + data[i+1:]
        i -= 2
    elif blockSize == size:
        total -= (i//2)*sumN(locations[i],size)
        total += (i//2)*sumN(blockLocation,size)
        blocks[blockNumber][2] = 0 #for good measure i guess
        blockNumber += 1
        data = data[:i] + "0" + data[i+1:]
        i -= 2
    elif blockSize < size:
        total -= (i//2)*sumN(locations[i] + size - blockSize, blockSize)
        total += (i//2)*sumN(blockLocation, blockSize)
        blocks[blockNumber][2] = 0 #for good measure i guess
        blockNumber += 1
        data = data[:i] + str(size - blockSize) + data[i+1:]
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
