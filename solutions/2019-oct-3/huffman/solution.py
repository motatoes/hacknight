import sys
from collections import defaultdict

class Node:
    c = None
    f = 0
    left = None
    right = None

    def __init__(self, **kwargs):
        self.c = kwargs.get('c', None)
        self.f = kwargs.get('f', 0)
        self.left = kwargs.get('left', None)
        self.right = kwargs.get('right', None)

        
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
def buildEncodingTree():
    tree = Node()

    return tree

# step 3, build encoding map
def buildEncodingMap():
    pass

# step 4, encode the file contents for compression
def encodeData():
    pass

# step 4.2, the decompression version of step 4 above
def decodeData():
    pass


if __name__ == "__main__":
    filename = sys.argv[1]

    # step 1
    print("building frequency table ...")
    freq = buildFrequencyTable(filename)
    print(freq)


    # step 2
    print("building huffman tree ...")

    # step 3
    print("compressing the file ....")
