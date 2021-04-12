import timeit

length=int(input('enter length of input numbers : '))


inputs=[]

for i in range(0,length):
	inputs.append(i)

print(inputs)



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
	start=timeit.default_timer()
	high=len(inputs)-1
	low=0
	flag=0
	while(low<=high):
		mid=(low+high)//2	
		if (inputs[mid]==querry):
			print('querry found at index ', mid)
			flag=1
			break
		elif(querry<inputs[mid]):
			high=mid-1
		elif(querry>inputs[mid]):
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

def make_binarysearchtree(inputs):

def find_binarysearchtree(querry):
								




	
linearsearch(inputs,20)	

binarysearch(inputs,20)


