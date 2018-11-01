import heapq
characterlist=[]
cleanlist=[]
letters=[]
mydict = {}

class Node:
	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None



def fileRead():
    with open('Gutenberg.txt') as f:
        while True:
            character = f.read(1)
            if not character:
                break
            else:
                characterlist.append(character)


def convertFile():
    for char in characterlist:
        if char.islower() or char == ' ' or char == '.' or char == ',' or char == '!' or char == '?' or char == ';':
            cleanlist.append(char)


def frequency():
    for char in cleanlist:
        if char in mydict:
            mydict[char] += 1
        else:
            mydict[char] = 1
    return mydict


def insertHeap():
    dict = frequency()
    for key in dict:
        ob = Node(key, dict[key])
        heapq.heappush(Q,(dict[key],ob))

def mergeNode():
    global ROOT
    while (len(Q)!=1):
        firstnode=heapq.heappop(Q)
        secondnode=heapq.heappop(Q)
        combine=Node("".join([firstnode[1].char,secondnode[1].char]),firstnode[1].freq+secondnode[1].freq)
        combine.left=firstnode[1]
        combine.right=secondnode[1]
        combine.freq = firstnode[1].freq+secondnode[1].freq
        ROOT = combine
        heapq.heappush(Q,(combine.freq, combine))


def traverseTree(node,bit):
    if node.left is None and node.right is None:
        print node.char, bit
    else:
        traverseTree(node.left, bit + '0')
        traverseTree(node.right, bit + '1')





Q=[]
root = None
heapq.heapify(Q)
fileRead()
convertFile()
insertHeap()
mergeNode()
traverseTree(ROOT,'')





