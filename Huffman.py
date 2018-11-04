import heapq
Q = []
newdict = {}
class Node:
	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None

    # Piazza post: https://iu.instructure.com/courses/1735890/external_tools/58924
	def __lt__(self, other):
		return self.freq < other.freq


# https://stackoverflow.com/questions/2988211/how-to-read-a-single-character-at-a-time-from-a-file-in-python
def fileRead():
	characterlist = []
	with open('Gutenberg.txt') as f:
		while True:
			character = f.read(1)
			if not character:
				break
			elif character.isupper():
				characterlist.append(character.lower())
			else:
				characterlist.append(character)
	return characterlist


def convertFile():
	cleanlist = []
	characterlist=fileRead()
	for char in characterlist:
		if char.islower() or char == ' ' or char == '.' or char == ',' or char == '!' or char == '?' or char == "'":
			cleanlist.append(char)
	return cleanlist


def countFrequency():
	mydict = {}
	cleanlist=convertFile()
	for char in cleanlist:
		if char in mydict:
			mydict[char] += 1
		else:
			mydict[char] = 1
	return mydict


def insertHeap():
	mydict = countFrequency()
	heapq.heapify(Q)
	for key in mydict:
		ob = Node(key, mydict[key])
		heapq.heappush(Q,(mydict[key],ob))
	return mydict

# Piazza post: https://iu.instructure.com/courses/1735890/external_tools/58924
def mergeNode():
	global parentNode
	while (len(Q)!=1):
		firstnode=heapq.heappop(Q)
		secondnode=heapq.heappop(Q)
		combine=Node("".join([firstnode[1].char,secondnode[1].char]),firstnode[1].freq+secondnode[1].freq)
		combine.left=firstnode[1]
		combine.right=secondnode[1]
		combine.freq = firstnode[1].freq+secondnode[1].freq
		parentNode = combine
		heapq.heappush(Q,(combine.freq, combine))


def printTree(node,bit):
	if node.left is None and node.right is None:
		print node.char, bit
		newdict[node.char]=len(bit)
	else:
		printTree(node.left, bit + '0')
		printTree(node.right, bit + '1')

def huffmanCalculation():
	cleanlist = convertFile()
	mydict=insertHeap()
	fivebitsum = len(cleanlist) * 5
	huffmansum=0
	for key in mydict:
		count=0
		if key in newdict:
				count=newdict[key]*mydict[key]
				huffmansum=huffmansum+count

	print "The text was encoded using {} bits".format(huffmansum)
	print "The text had {} valid characters".format(len(cleanlist))
	print "Using a 5-bit fixed length encoding, this would have been {} bits long".format(fivebitsum)
	print "So we saved {} bits!".format(fivebitsum - huffmansum)





parentNode = None
fileRead()
convertFile()
countFrequency()
mydict=insertHeap()
print "FREQUENCY"
print mydict
print "\n"
mergeNode()
print "HUFFMAN CODE"
printTree(parentNode,'')
print "\n"
huffmanCalculation()









