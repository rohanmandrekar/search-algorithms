import timeit
import random

length=int(input('enter length of input numbers : '))


inputs=[]


while (len(inputs)!=length):
	r=random.randint(0,length)
	if (r not in inputs): 
		inputs.append(r)

print(inputs)

querry=int(input('Enter the number you want to find : '))

def linearsearch(inputs,querry):
	start=timeit.default_timer()

	flag=0
	pos=0
	for number in inputs:
		if (querry==number):
			print('querry found at index ',pos)
			flag=1
			break
		pos+=1	
	stop=timeit.default_timer()		
	if (flag==0):
		print('querry not found in given inputs')
	print('runtime for linear search : ',stop-start)



def binarysearch(inputs,querry):

	temp_inputs = inputs
	temp_inputs.sort()
	print('temp inp',temp_inputs)

	start=timeit.default_timer()
	high=len(temp_inputs)-1
	low=0
	flag=0
	while(low<=high):
		mid=(low+high)//2	
		if (temp_inputs[mid]==querry):
			print('querry found at index ', mid)
			flag=1
			break
		elif(querry<temp_inputs[mid]):
			high=mid-1
		elif(querry>temp_inputs[mid]):
			low=mid+1
	if (flag==0):
		print('querry not found in inputs')	
	stop=timeit.default_timer()
	print('runtime of binary search : ',stop-start)				



class binarysearchtree:

	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None

	def insert_node(self,data):
		

		if (data > self.data):
			if self.right is None:
				self.right=binarysearchtree(data)
			else:
				self.right.insert_node(data)

		elif (data < self.data):
			if self.left is None:
				self.left=binarysearchtree(data)
			else:
				self.left.insert_node(data)

	def find(self,querry):

		if (querry==self.data):
			print('querry found in binary search tree')

		if (querry > self.data):
			if (self.right is None):
				print('querry not found in inputs')
			else:
				self.right.find(querry)

		if (querry < self.data):
			if (self.left is None):
				print('querry not found in inputs')
			else:
				self.left.find(querry)

def make_binarysearchtree(inputs,querry):

	root=binarysearchtree(inputs[0])

	for i in range(1,len(inputs)):
		root.insert_node(inputs[i])

	start=timeit.default_timer()	
	root.find(querry)
	stop=timeit.default_timer()
	print('runtime for binary search tree : ',stop-start)	


class NullNode:
	def __init__(self, parent):
		self.val = None
		self.left = None
		self.right = None
		self.parent = parent
		self.color = "BLACK"

class RBNode:
	def __init__(self, newval):
		self.val = newval
		self.left = NullNode(self)
		self.right = NullNode(self)
		self.parent = None
		self.color = 'RED'


        
# https://github.com/JinheonBaek/DS-RedBlackTree/blob/master/term-project/tree.py
class redblacktree:
	def __init__(self):
		self.root = None

	def search(self, tree, val):
		if self.root is None:
			#print("That RedBlack Tree do not have any Node")
			return None
		if tree.val is None:
			print(val, "is not in the red-black tree")
			return tree
		if tree.val > val:
			return self.search(tree.left, val)
		elif tree.val < val:
			return self.search(tree.right, val)
		else:
			print('querry found in red-black tree')
			return tree

	def insert(self, tree, n):
			# init
			y = None
			x = self.root
			# self.insertNode += 1

			# search inserting place
			while x is not None and x.val is not None:
				y = x
				if n.val < x.val:
				    x = x.left
				else:
				    x = x.right

				# insert new node
			n.parent = y
			if y is None:
				self.root = n
			elif n.val < y.val:
				y.left = n
			else:
				y.right = n

			# fix up RBT
			self.RBT_Insert_Fixup(self, n)

	def RBT_Insert_Fixup(self, tree, n):
		while n.parent is not None and n.parent.parent is not None and n.parent.color is 'RED':
			if n.parent == n.parent.parent.left:
				y = n.parent.parent.right
				if y is not None and y.color == "RED":
					n.parent.color = "BLACK"
					y.color = "BLACK"
					n.parent.parent.color = "RED"
					n = n.parent.parent
				else:
					if n == n.parent.right:
						n = n.parent
						self.Left_Rotate(tree, n)
					n.parent.color = "BLACK"
					n.parent.parent.color = "RED"
					self.Right_Rotate(tree, n.parent.parent)
			else:
				y = n.parent.parent.left
				if y is not None and y.color == "RED":
					n.parent.color = "BLACK"
					y.color = "BLACK"
					n.parent.parent.color = "RED"
					n = n.parent.parent
				else:
					if n == n.parent.left:
						n = n.parent
						self.Right_Rotate(tree, n)
					n.parent.color = "BLACK"
					n.parent.parent.color = "RED"
					self.Left_Rotate(tree, n.parent.parent)
		self.root.color = "BLACK"

	def Left_Rotate(self, tree, x):
            # set y
		y = x.right

		# insert subtree of y into x
		x.right = y.left
		if y.left is not None:
			y.left.parent = x

		# link x's parent to y
		y.parent = x.parent
		if x.parent is None:
			tree.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y

		# put x on y's left
		y.left = x
		x.parent = y

	def Right_Rotate(self, tree, x):
		# set y
		y = x.left

		# insert subtree of y into x
		x.left = y.right
		if y.right is not None:
			y.right.parent = x

		# link x's parent to y
		y.parent = x.parent
		if x.parent is None:
			tree.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y

		# put x on y's right
		y.right = x
		x.parent = y


def make_redblacktree(inputs,querry):

	rbt=redblacktree()

	for i in inputs:
		rbt.insert(rbt.root,RBNode(i))
	start=timeit.default_timer()	
	rbt.search(rbt.root,querry)	
	stop=timeit.default_timer()
	print('search time for red black tree : ',stop-start)



	
linearsearch(inputs,querry)	

binarysearch(inputs,querry)

make_binarysearchtree(inputs,querry)

make_redblacktree(inputs,querry)

