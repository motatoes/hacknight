import sys
from math import ceil
from collections import defaultdict
import heapq

"""
this solution reads from a file

"""

class Node:
    # the character which this node represents, if any
    c = None

    # the frequency of occurence for this character
    f = 0

    # pointers to the left and right child
    left = None
    right = None

    def __init__(self, **kwargs):
        self.c = kwargs.get('c', None)
        self.f = kwargs.get('f', 0)
        self.left = kwargs.get('left', None)
        self.right = kwargs.get('right', None)

    def __lt__(self, other):
        return self.f < other.f

# step 1, build a frequency table from the stream of chatactars
def buildFrequencyTable(filepath):
    freq = defaultdict(int)
    f = open(filepath, 'r')
    while True:
        c = f.read(1)
        if not c:
            break
        freq[c] += 1

    f.close()
    return freq

# step 2, build the huffman tree
def buildEncodingTree(freqMap):

    priority = []

    for key,value in freqMap.items():
        heapq.heappush(priority, Node(c=key, f = value))

    while (len(priority) > 1):
        s1 = heapq.heappop(priority)
        s2 = heapq.heappop(priority)
        f = s1.f + s2.f
        heapq.heappush(priority, Node(left=s1, right=s2, f=f))

    return priority[0]

# step 3, build encoding map
def buildEncodingMap(tree):
    charMapping = dict()

    def traverse(root, prefix=''):
        if root is None: return
        if root.c is not None:
            charMapping[root.c] = prefix

        traverse(root.left, prefix=prefix+'0')
        traverse(root.right, prefix=prefix + '1')

    traverse(tree)
    return charMapping

# step 4, encode the file contents for compression
def encodeData(inputPath, charMapping, outputPath):
    f = open(inputPath, 'r')
    out_file = open(outputPath, 'wb')
    towrite = ""
    while True:
        c = f.read(1)
        if not c:
            break
        towrite += charMapping[c]
        # if we have complete a byte-length string, add it to the file
        if len(towrite) >= 8:
            out_file.write(int(towrite[:8],2).to_bytes(1, 'big'))
            towrite = towrite[8:]
        # towrite = int(charMapping[c], 2).to_bytes(ceil(len(charMapping[c])/8), 'big')

    # we need to pad zeros in the end to complete the last byte
    towrite = towrite + "0" * (8-len(towrite))
    out_file.write(int(towrite,2).to_bytes(1, 'little'))

    out_file.close()


# step 4.2, the decompression version of step 4 above
def decodeData(inputPath, tree):
    
    current_node = tree

    f = open(inputPath, 'rb')
    res = ""
    while True:
        c = f.read(1)
        nxt = f.read(1)
        f.seek(-1,1)


        if not nxt:
            break
        
        ival = c[0]
        for i in range(7,-1,-1):
            bit = ival >> i & 1
            # print(bit)
            if bit == 1:
                current_node = current_node.right
            else:
                current_node = current_node.left

            if current_node.c is not None:
                # print(current_node.c)
                res += current_node.c
                current_node = tree

    # remove trailing zeros
    ival = c[0]
    print(bin(ival))
    if ival > 0:
        trailing = 0
        while ival << 7 & 0b10000000 == 0:
            ival = ival >> 1
            trailing += 1

        for i in range(7-trailing,-1,-1):
            bit = ival >> i & 1
            # print(bit)
            if bit == 1:
                current_node = current_node.right
            else:
                current_node = current_node.left

            if current_node.c is not None:
                # print(current_node.c)
                res += current_node.c
                current_node = tree



    return res

if __name__ == "__main__":
    filename = sys.argv[1]

    # step 1
    print("building frequency table ...")
    freq = buildFrequencyTable(filename)
    print(freq)

    # step 2
    print("building huffman tree ...")
    tree = buildEncodingTree(freq)
    # print(tree)

    # step 3
    print("building the encoding map ...")
    encodeMap = buildEncodingMap(tree)
    print(encodeMap)

    # step 4
    print("writing the resulting file ...")
    outputPath = filename + ".huf"
    encodeData(filename, encodeMap, outputPath)

    # step 5
    print("uncompressing the compresssed file")
    res = decodeData(outputPath, tree)
    print("res:", res)


