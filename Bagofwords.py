import os.path
import math

def lowerspilt(l):
	empty=''
	for i in range(len(l)):
		if ord(l[i])>=97 and ord(l[i])<=122:
			empty=empty+l[i]
		elif ord(l[i])==32:
			empty=empty+l[i]
		else:
			i+=1
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
	print("The % of similarty between " + list[i] + " and "+ list[j] +" is " + str(similarity(z,p)))	

path ="C:/Users/welcome/Desktop/20176108 CSPP1_Proaject/file2"
list = os.listdir(path)
os.chdir(path) 

for i in range(len(list)):
	for j in range (i+1,len(list)):
		if i==j:
			pass
		else:
			file1=open(list[i],'r').read().lower()
			file2=open(list[j],'r').read().lower()
			getOutput(file1,file2)