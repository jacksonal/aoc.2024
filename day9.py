from util import getFileContents
import operator
diskmap = getFileContents('input.txt')
diskblocks = []
#print(len(diskmap))
for i,val in enumerate(diskmap):
    size = int(val)
    if i % 2 == 0: #file block
        id = str(i//2)
        #print('fileid', id, 'size', size)
        diskblocks.extend([id]*size)
    else: #freespace block
        diskblocks.extend('.'*size)
#print(diskblocks)

blockstack = diskblocks.copy()
packeddisk = []
for i,block in enumerate(diskblocks):
    if len(blockstack) <=i:
        break
    if block == '.':
        popBlock = blockstack.pop()
        while(popBlock == '.'):
            popBlock = blockstack.pop()
        packeddisk.append(popBlock)
    else:
        packeddisk.append(block)
#print(packeddisk)

print(sum(map(lambda x: x[0] * x[1],[(i, int(fileid)) for i,fileid in enumerate(packeddisk)])))