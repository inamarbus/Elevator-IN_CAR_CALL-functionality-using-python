
import os
import time
x=0
y=0
#DOORS
def doors():
	print("DOORS OPENNING")
	time.sleep(5)
	print("DOORS CLOSING")
	time.sleep(2)
#setup
def setup(fla):
	#fl = int(input("Enterfloor"))
	for i in range(1,fla+1):
	        print (i)
		time.sleep(1)
	return (i)

#flooring_decreasing
def flooring_dec(top_floor,fl):
	#fl = int(input("Enterfloor"))
	for j in range(top_floor,fl-1,-1):

	        print (j)
		time.sleep(1)

#flooring_increasing
def flooring_inc(top_floor,fl):
	#fl = int(input("Enterfloor"))
	for k in range(top_floor,fl+1):

	        print (k)
		time.sleep(1)

	
n = int(input("Enter the total number of floors: "))
x=n
# check the input value
if (n<1 or n==0):
	print ("n should be greater than 1")
	exit()
else:
	setup(n)


#while part

while 1:	
	f = int(input("Enter the Floor number:"))
	
#for j in range(1,n+1):
	if (f<1 or f==0):

		print ("f should be greater than 1")
		exit()

	if (f>n): 	
		
		flooring_inc(n,f)
	if (f<n):
		flooring_dec(n,f)

	doors()

	n=f


