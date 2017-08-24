import os.path
import math

def lowerspilt(l):
	empty=''
	for i in range(len(l)):
		if 48<=ord(l[i])<=57 or 97<=ord(l[i])<=122 or ord(l[i])==95 :
			empty=empty+l[i]
		else:
			empty=empty+' '
	return empty

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
def getOutput(file1,file2):
	a=lowerspilt(file1).split()
	b=lowerspilt(file2).split()
	x=(dict(a))
	y=(dict(b))
	z=(dotproduct(x,y))
	p=(sumofsquaresfrequency(x,y))
#	print("The % of similarty between " + list[i] + " and "+ list[j] +" is " + str(
	l=similarity(z,p)
	return (l)	

path ="C:/Users/welcome/Desktop/20176108 CSPP1_Proaject/file1"
list = os.listdir(path)
os.chdir(path)
u=["  "] 
for i in range(len(list)):
	u.append(list[i])
print(u)
for i in range(len(list)):
	v=[]
	for j in range (0,len(list)):
		if i==j:
			v.append("Nil")
		else:
			file1=open(list[i],'r').read().lower()
			file2=open(list[j],'r').read().lower()
			k=getOutput(file1,file2)
			v.append(k)
	print(list[i],v)