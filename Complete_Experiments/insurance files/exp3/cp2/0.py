import string

import math
import random
import numpy as np

    
N = 1000
cp = 0

E= int(math.floor(cp*N))

TM=np.zeros((N,N))
print(E)
    
T_arr=[-1]*N

count=E

while(count!=0):
    Temp1 = random.randint(0,N-1)
    Temp2 = random.randint(0,N-1)
    if(TM[Temp1, Temp2]==0 and Temp1 != Temp2 and TM[Temp2, Temp1]==0 and Temp1<Temp2):
        TM[Temp1,Temp2]=1
        count=count-1



temp=0;
for i in range(0, N):
    if T_arr[i]==-1:
        T_arr[i]=temp
        temp=temp+1
    for j in range(0, N):
        if TM[i,j]!= 0:
            T_arr[j]=T_arr[i]



np.random.shuffle(T_arr)




f=open("0.txt","w")
for i in T_arr:
    rnd1=random.randint(100000,1000000)
    rnd2=random.randint(10000,100000)
    str1=''.join(random.choices(string.ascii_lowercase,k=5))
    rnd3=random.randint(30000,40000)
    str2=''.join(random.choices(string.ascii_lowercase,k=6))
    f.write("useradd user"+str(i)+","+str(rnd1)+","+str(rnd2)+","+str1+","+str2+","+str(rnd3)+",US"+"\n")



