import sys
from collections import defaultdict
import heapq

"""
this solution reads from a string in memory, it is simpler to implement since it
avoide file IO hackery
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
def buildFrequencyTable(word):
    freq = defaultdict(int)
    for i in range(len(word)):
        c = word[i]
        freq[c] += 1

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
def encodeData(word, charMapping):
    encodedStr = ""
    for i in range(len(word)):
        c = word[i]
        if not c:
            break
        encodedStr += charMapping[c]

    return encodedStr

# step 4.2, the decompression version of step 4 above
def decodeData(encodedString, tree):
    
    current_node = tree
    res = ""
    for i in range(len(encodedString)):
        bit = int(encodedString[i])

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
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = "lorem ipsum dolor sit amet"

    print("we will compress the word:",  word)
    # step 1
    print("building frequency table ...")
    freq = buildFrequencyTable(word)
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
    print("encoding the data ...")
    encodedString = encodeData(word, encodeMap)
    print(encodedString)
    # step 5
    print("uncompressing the data again ...")
    res = decodeData(encodedString, tree)
    print("res:", res)

    print("-------")
    originalLen = (8 * len(word))
    encodedLen = (len(encodedString))
    saving = round( (1 - ( encodedLen / originalLen)) * 100, 2 )
    print(f"we went down from {originalLen} bytes to {encodedLen} bytes. compression ratio: {saving} %")

