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

	
linearsearch(inputs,20)	

binarysearch(inputs,20)


