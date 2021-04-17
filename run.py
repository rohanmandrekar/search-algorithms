import timeit
import random
import sys

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


class Null:
	def __init__(self,parent):
		self.data=None
		self.left=None
		self.right=None
		self.color='black'
		self.parent=parent

class RBNode:
	def __init__(self,data):
		self.data=data
		self.left=Null(self)
		self.right=Null(self)
		self.parent=None
		self.color='red'


# reference : https://github.com/JinheonBaek/DS-RedBlackTree/blob/master/term-project/tree.py

class redblacktree:

	def __init__(self):
		self.root=None

	def insert_node(self,tree,n):

		root=self.root
		y=None

		while root is not None and root.data is not None:

			y=root

			if (n.data<root.data):
				root= root.left

			else:
				root= root.right	

			n.parent=y
			if y is None:
				self.root = n
			elif n.data < y.data:
			    y.left = n
			else:
			    y.right = n

		self.fixRBT(sef,n)

	def find(self, tree , querry):

		
		if tree.data > querry:
			return self.search(tree.left, querry)
		elif tree.data < querry:
			return self.search(tree.right, querry)
		else:
			print('querry found in red black tree')
			return tree		    				
		if tree.data is None:
			print(querry, "is not in the red black tree")
			return tree

	def fixRBT(self, tree, n):
		while n.parent is not None and n.parent.parent is not None and n.parent.color is 'red':
			if n.parent = n.parent.parent.left:
				y=n.parent.parent.right:
				if y is not None and y.color=='red':
					n.parent.color='black'
					y.color='black'
					n.parent.parent.color='red'
					n=n.parent.parent
				else:
					if n== n.parent.right:
						n=n.parent
						self.left_rotate(tree,n)
					n.parent.color='red'
					n.parent.parent.color='black'
					self.right_rotate(tree,n.parent.parent)

			else:
				y=n.parent.parent.left
				if y is not None and y.color=='red'
					n.parent.color='black'
					y.color='black'
					n.parent.parent.color='red'
					n=n.parent.parent
				else:
					if n==n.parent.left
						n=n.parent
						self.right_rotate(tree,n)

					n.parent.color='black'
					n.parent.parent.color='red'
					self.left_rotate(tree, n.parent.parent)

			self.root.color='black'

	def left_rotate(self, tree, x):
	
	def right_rotate(self, tree, x):



        

	
linearsearch(inputs,querry)	

binarysearch(inputs,querry)

make_binarysearchtree(inputs,querry)

# make_redblacktree(inputs,20)

