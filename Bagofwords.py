import math
file1=open('sir.py','r').read().lower()
file2=open('tuple.py','r').read().lower()

def lowerspilt(l):
	empty=''
	for i in l:
		if ord(i)>=97 and ord(i)<=122:
			empty=empty+i
		else:
			empty=empty+' '
	return (empty)
				

def dict(l):
	mydict={}
	for i in l:
		if i not in mydict:
			mydict[i]=1
		else:
			mydict[i]+=1
	return mydict

def dotproduct(x,y):
	sum=0
	for i in x:
		for j in y:
			if i==j:
				mul=x[i]*y[j]
				sum=sum+mul
	return (sum)

def sumofsquaresfrequency(x,y):
	sum1=0
	sum2=0
	for i in x:
		sum1=sum1+(x[i]**2)
	for i in y:
		sum2=sum2+(y[i]**2)
	m=math.sqrt(sum1)
	n=math.sqrt(sum2)
	return(m*n)
	
def similarity(sum,l):
	cos=(sum/l)*100
	return(cos)

a=lowerspilt(file1).split()
b=lowerspilt(file2).split()

x=(dict(a))
y=(dict(b))
z=(dotproduct(x,y))
p=(sumofsquaresfrequency(x,y))
print("The % of similarty is",similarity(z,p))