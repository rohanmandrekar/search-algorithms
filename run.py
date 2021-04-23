import timeit
import random
from tkinter import *


# from flask import Flask,request,render_template,redirect,url_for,make_response

# app = Flask(__name__)



def linearsearch(inputs,querry):
	# start=timeit.default_timer()

	flag=0
	pos=0
	for number in inputs:
		if (querry==number):
			print('querry found at index ',pos)
			found=True
			flag=1
			stop=timeit.default_timer()	
			# print('runtime for linear search : ',stop-start)
			return found
		pos+=1	
	# stop=timeit.default_timer()		
	if (flag==0):
		print('querry not found in given inputs')
		found=False
	# print('runtime for linear search : ',stop-start)
	return found




def binarysearch(temp_inputs,querry):

	

	# start=timeit.default_timer()
	high=len(temp_inputs)-1
	low=0
	flag=0
	while(low<=high):
		mid=(low+high)//2	
		if (temp_inputs[mid]==querry):
			print('querry found at index ', mid)
			flag=1
			found=True
			# stop=timeit.default_timer()
			# print('runtime of binary search : ',stop-start)
			return found
		elif(querry<temp_inputs[mid]):
			high=mid-1
		elif(querry>temp_inputs[mid]):
			low=mid+1
	if (flag==0):
		found=False
		print('querry not found in inputs')	
	# stop=timeit.default_timer()
	# print('runtime of binary search : ',stop-start)
	# stop=start=time
	return found			



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

	def findbst(self,querry):

		if (querry==self.data):
			label=Label(tk,text='querry found in binary search tree.')
			label.pack()
			return 
		if (querry > self.data):
			if (self.right is None):
				label=Label(tk,text='querry not found in binary search tree.')
				label.pack()
				return False
			else:
				self.right.findbst(querry)

		if (querry < self.data):
			if (self.left is None):
				label=Label(tk,text='querry not found in binary search tree.')
				label.pack()
				# found=False
				return False
			else:
				self.left.findbst(querry)

def make_binarysearchtree(inputs,querry):

	root=binarysearchtree(inputs[0])

	for i in range(1,len(inputs)):
		root.insert_node(inputs[i])
	start=timeit.default_timer()	
	found=root.findbst(querry)
	stop=timeit.default_timer()
	time=stop-start
	
	return found,time


class RBNode:
	def __init__(self, newdata):
		self.data = newdata
		self.left = NullNode(self)
		self.right = NullNode(self)
		self.parent = None
		self.color = 'RED'

class NullNode:
	def __init__(self, parent):
		self.data = None
		self.left = None
		self.right = None
		self.parent = parent
		self.color = "BLACK"


        
# https://github.com/JinheonBaek/DS-RedBlackTree/blob/master/term-project/tree.py
class redblacktree:
	def __init__(self):
		self.root = None

	def find(self, tree, querry):
		if self.root is None:
			return None
		if tree.data is None:
			print("querry not found in red black tree")
			found=False
			return found
		if tree.data > querry:
			return self.find(tree.left, querry)
		elif tree.data < querry:
			return self.find(tree.right, querry)
		else:
			print('querry found in red black tree')
			found=True
			return found

	def insert_node(self, tree, n):
			
			y = None
			x = self.root
			
			while x is not None and x.data is not None:
				y = x
				if n.data < x.data:
				    x = x.left
				else:
				    x = x.right

				
			n.parent = y
			if y is None:
				self.root = n
			elif n.data < y.data:
				y.left = n
			else:
				y.right = n

			
			self.fix_insert(self, n)

	def fix_insert(self, tree, n):
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
						self.leftrotate(tree, n)
					n.parent.color = "BLACK"
					n.parent.parent.color = "RED"
					self.rightrotate(tree, n.parent.parent)
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
						self.rightrotate(tree, n)
					n.parent.color = "BLACK"
					n.parent.parent.color = "RED"
					self.leftrotate(tree, n.parent.parent)
		self.root.color = "BLACK"

	def leftrotate(self, tree, x):
        
		y = x.right

		
		x.right = y.left
		if y.left is not None:
			y.left.parent = x

		
		y.parent = x.parent
		if x.parent is None:
			tree.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y

		
		y.left = x
		x.parent = y

	def rightrotate(self, tree, x):
		
		y = x.left

		
		x.left = y.right
		if y.right is not None:
			y.right.parent = x

		
		y.parent = x.parent
		if x.parent is None:
			tree.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y

		
		y.right = x
		x.parent = y


def make_redblacktree(inputs,querry):

	rbt=redblacktree()

	for i in inputs:
		rbt.insert_node(rbt.root,RBNode(i))
	start=timeit.default_timer()
	found=rbt.find(rbt.root,querry)	
	stop=timeit.default_timer()
	time=stop-start
	return found,time



# @app.route("/",methods=["GET","POST"])
# def home():

# 	return render_template('home.html')





	
# a=linearsearch(inputs,querry)

# b=binarysearch(inputs,querry)

# c=make_binarysearchtree(inputs,querry)

# d=make_redblacktree(inputs,querry)
# print(inputs)
# li=[a,b,c,d]
# print(li)

def linearsearchb(inputs,querry):
	label=Label(tk,text='')
	label.pack()
	start=timeit.default_timer()
	flag=linearsearch(inputs,querry)
	stop=timeit.default_timer()
	time= stop-start
	if flag==True:
		text="querry found in linear search. time taken =  %f" %time
	else:
		text="querry not found in linear search. time taken : %f"%time
	
	label=Label(tk,text=text)
	label.pack(ipadx=10,ipady=10)

def binarysearchb(inputs,querry):
	temp_inputs = inputs.copy()
	temp_inputs.sort()
	print('temp inp',temp_inputs)
	label=Label(tk,text='')
	label.pack()
	start=timeit.default_timer()
	flag=binarysearch(temp_inputs,querry)
	stop=timeit.default_timer()
	time= stop-start
	if flag==True:
		text="querry found in binary search. time taken =  %f" %time
	else:
		text="querry not found in binary search. time taken : %f"%time
	
	label=Label(tk,text=text)
	label.pack(ipadx=10,ipady=10)

def binarysearchtreeb(inputs,querry):
	label=Label(tk,text='')
	label.pack()
	start=timeit.default_timer()
	flag,time1=make_binarysearchtree(inputs,querry)
	stop=timeit.default_timer()
	time= stop-start
	label=Label(text='time taken : %f'%time1)
	label.pack()
	label2=Label(tk,text="build and search time = %f" %time)
	label2.pack()
	
	# label=Label(tk,text=text)
	# label.pack(ipadx=10,ipady=10)

def redblackb(inputs,querry):
	label=Label(tk,text='')
	label.pack()
	start=timeit.default_timer()
	flag,time1=make_redblacktree(inputs,querry)
	stop=timeit.default_timer()
	time= stop-start
	if flag==True:
		text="querry found in Red-Black Tree.  search time taken =  %f" %time1
		text1="build and search time = %f" %time
	else:
		text="querry not found in Red-Black Tree. time taken : %f"%time1
		text1="build and search time = %f" %time
	
	label=Label(tk,text=text)
	label.pack(ipadx=10,ipady=10)
	label2=Label(tk,text=text1)
	label2.pack()			




# if __name__ == "__main__":
#     app.run(host= '0.0.0.0', port=9000, debug=True)


def generate():
	x=e.get()
	length=int(x)
	inputs=[]
	while (len(inputs)!=length):
		r=random.randint(0,length)
		if (r not in inputs): 
			inputs.append(r)

	print(inputs)
	y=e2.get()
	querry=int(y)
	
	



	linearbutton=Button(tk,text='Linear Search',command=linearsearchb(inputs,querry))
	linearbutton.pack()
	binarybutton=Button(tk,text='Binary Search', command=binarysearchb(inputs,querry))
	binarybutton.pack()
	bstbutton=Button(tk,text='Binary Search Tree',command=binarysearchtreeb(inputs,querry))
	bstbutton.pack()
	rbtbutton=Button(tk,text='Red Black Tree Search',command=redblackb(inputs,querry))
	rbtbutton.pack()

# def run(inputs,e2):
	

# 	linearbutton=Button(tk,text='Linear Search',command=linearsearchb(inputs,querry))
# 	linearbutton.pack()
# 	binarybutton=Button(tk,text='Binary Search', command=binarysearchb(inputs,querry))
# 	binarybutton.pack()
# 	bstbutton=Button(tk,text='Binary Search Tree',command=binarysearchb(inputs,querry))
# 	bstbutton.pack()
# 	rbtbutton=Button(tk,text='Red Black Tree Search',command=redblackb(inputs,querry))
# 	rbtbutton.pack()	

# def clean():
# 	tk.children.clear
# 	label1=Label(tk,text='Enter the no. of inputs u want')
# 	label1.pack()



# 	e=Entry(tk, width=20)
# 	e.pack()

# 	label2=Label(tk,text='Enter the number you want to find')
# 	label2.pack()

# 	e2=Entry(tk,width=20)
# 	e2.pack()
# 	# length=int(input('length : '))
# 	btn=Button(tk,text='submit', command=generate)
# 	btn.pack()





tk=Tk()
tk.geometry=("1920x1080")

label1=Label(tk,text='Enter the no. of inputs u want')
label1.pack()

e=Entry(tk, width=20)
e.pack()

label2=Label(tk,text='Enter the number you want to find')
label2.pack()

e2=Entry(tk,width=20)
e2.pack()
# length=int(input('length : '))
btn=Button(tk,text='submit', command=generate)
btn.pack()

# btn2=Button(tk,text='Clear all outputs', command=clean)
# btn2.pack()
# label2=Label(tk,text='Enter the number you want to find')
# label2.pack()
# e2=Entry(tk,width=20)
# e2.pack()
# btn2=Button(tk,command=run)
# btn2.pack()



# length1=int(e.get())

# label1.pack()


# submitbtn=Button(tk, text='submit', command=generate())


# inputs=[]


# while (len(inputs)!=length):
# 	r=random.randint(0,length)
# 	if (r not in inputs): 
# 		inputs.append(r)

# print(inputs)

# querry=int(input('Enter the number you want to find : '))



tk.mainloop()