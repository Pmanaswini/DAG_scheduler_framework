import string

import math
import random
import numpy as np

    
N = 600
cp=5
E0 =int(math.floor((cp*N)/100))
print(E0)

Accounts=[None] * E0
for i in range(0,E0):
    Accounts[i]="a"+str(i)

T_arr=[None]*N


temp=int(math.floor(N/E0))


k=0
for i in range(0,E0):
    for j in range(0,temp):
        com = i
        T_arr[k]=str(com)
        k=k+1


np.random.shuffle(T_arr)




f=open("600.txt","w")
for i in T_arr:
    rnd1=random.randint(100000,1000000)
    rnd2=random.randint(10000,100000)
    str1=''.join(random.choices(string.ascii_lowercase,k=5))
    rnd3=random.randint(30000,40000)
    str2=''.join(random.choices(string.ascii_lowercase,k=6))
    f.write("useradd user"+str(i)+","+str(rnd1)+","+str(rnd2)+","+str1+","+str2+","+str(rnd3)+",US"+"\n")



  

