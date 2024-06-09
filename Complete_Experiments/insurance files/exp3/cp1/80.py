import string

import math
import random
import numpy as np
    
N = 1000
cp = 80

Te= int(math.floor(cp*N/100))
T0 = N - Te

Accounts=[None] * N
for i in range(0, T0):
    Accounts[i]=str(i)

Acc= int(math.ceil(0.1*Te))

for i in range(0, Acc):
    Accounts[T0+i]=str(i+T0)

temp_2 = T0;
T_arr=[None] * N
T_arr[ 0: T0 ]= Accounts[ 0 : T0];

print(T0,Acc)

for i in range(temp_2,N):
    Temp_acc = random.randint(0,Acc-1)+T0
    T_arr [ i ] = str(Temp_acc)

np.random.shuffle(T_arr)

    

f=open("80.txt","w")
for i in T_arr:
    rnd1=random.randint(100000,1000000)
    rnd2=random.randint(10000,100000)
    str1=''.join(random.choices(string.ascii_lowercase,k=5))
    rnd3=random.randint(30000,40000)
    str2=''.join(random.choices(string.ascii_lowercase,k=6))
    f.write("useradd user"+str(i)+","+str(rnd1)+","+str(rnd2)+","+str1+","+str2+","+str(rnd3)+",US"+"\n")



