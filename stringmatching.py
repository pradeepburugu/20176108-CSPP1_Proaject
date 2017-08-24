import os.path
def splitfunction(p):
	em=''
	for i in range(len(p)):
		if 48<=ord(p[i])<=57 or 97<=ord(p[i])<=122 or ord(p[i])==95 :
			em=em+p[i]
		else:
			em=em+' '
	return em

def compare(s,l):
	temp=0
	for i in range(len(s)):
		for j in range(len(l)):
			r=[]
			while i<len(s) and j<len(l) and s[i]==l[j]:
				r.append(s[i])
				i=i+1
				j=j+1
			#if len(r)!=0:
			r=' '.join(r)
			r=r.strip()
			if len(r)>temp:
				temp=len(r)
	return(temp)



def output(f1,f2):
	s=splitfunction(f1).split()
	l=splitfunction(f2).split()
	totalle=len(f1)+len(f2)
	cm=compare(s,l)
	percentage=((cm*2/totalle)*100)

	print('The similarity between',list[i],'and',list[j],percentage)

path='C:/Users/welcome\Desktop/20176108 CSPP1_Proaject/file3'
list=os.listdir(path)
os.chdir(path)
for i in range(len(list)):
	for j in range(i+1,len(list)):
		if i==j:
			pass
		else:
			f1=open(list[i],'r').read().lower()
			f2=open(list[j],'r').read().lower()
			output(f1,f2)