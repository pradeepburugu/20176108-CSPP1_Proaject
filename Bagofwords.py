import math
file1=open('sir.py','r').read().lower().replace(',',' ').replace('.',' ').split()
file2=open('tuple.py','r').read().lower().replace(',',' ').replace('.',' ').split()

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

x=(dict(file1))
y=(dict(file2))
z=(dotproduct(x,y))
p=(sumofsquaresfrequency(x,y))
print("The % of similarty is",similarity(z,p))









