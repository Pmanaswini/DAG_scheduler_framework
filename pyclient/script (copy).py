import os
import time
import subprocess
import re
with open('keyGen.txt', 'r') as file:
    for line in file:
        subprocess.call(line.strip(), shell=True)
if os.path.exists('batches.txt'):
    os.remove('batches.txt')
os.rename('iniDepo.txt', 'batches.txt')
os.system("./simplewallet")
time.sleep(60)
current_dir = os.path.dirname(os.getcwd())
parent_dir = os.path.dirname(current_dir)
os.chdir(parent_dir)
os.chdir('sawtooth-core/validator')
os.remove('timing_computation.txt')
os.remove('DS_computation.txt')
current_dir = os.path.dirname(os.getcwd())
parent_dir = os.path.dirname(current_dir)
os.chdir(parent_dir)
os.chdir('sawtooth-core/pyclient')
command = "sawtooth batch list --url http://rest-api:8008"
with open("output.txt", "w") as f:
    subprocess.run(command, shell=True, stdout=f)
with open("output.txt", "r") as f:
    lines = len(f.readlines())
os.remove('batches.txt')
os.rename('testFile.txt', 'batches.txt')
#numBlocks = int(input('Enter no of blocks:'))
numBlocks=1
curr=lines
#print("Before entering while Curr",curr)
while(numBlocks>0):
    command = "sawtooth batch list --url http://rest-api:8008"
    with open("output.txt", "w") as f:
        subprocess.run(command, shell=True, stdout=f)
    with open("output.txt", "r") as f:
        lines = len(f.readlines())
    #print("Curr",curr)
    #print("lines",lines)
    if lines==curr:
        os.system("./simplewallet")
        curr=curr+1
        numBlocks=numBlocks-1
    else:
        print("Waiting for response")
    time.sleep(60)

n=0
current_dir = os.path.dirname(os.getcwd())
parent_dir = os.path.dirname(current_dir)
os.chdir(parent_dir)
os.chdir('sawtooth-core/validator')

with open('timing_computation.txt', 'r') as file:
    total = 0.0
    for line in file:
        #print(line)
        # Extract the numbers from the line
        numbers = re.findall('\d+\.\d+', line)
        #print(numbers)
        if len(numbers) > 0:
            for number in numbers:
                total += float(number)
                n=n+1
DS_LL = 0.0
DS_ADJ = 0.0
DS_Tree = 0.0
DS_SV = 0.0

with open("DS_computation.txt", "r") as file:
    value=0
    for line in file:
        if line.startswith("LL_DAG:"):
            value = float(line.split(":")[1])
            DS_LL += value

with open("DS_computation.txt", "r") as file:
    value=0
    for line in file:
        if line.startswith("ADJ_DAG:"):
            value = float(line.split(":")[1])
            DS_ADJ += value

with open("DS_computation.txt", "r") as file:
    value=0
    for line in file:
        if line.startswith("TREE:"):
            value = float(line.split(":")[1])
            DS_Tree += value

with open("DS_computation.txt", "r") as file:
    value=0
    for line in file:
        if line.startswith("SMART:"):
            value = float(line.split(":")[1])
            DS_SV += value

if DS_LL>0:
    print("LL DAG data struction creation time:", DS_LL)
if DS_ADJ>0:
    print("ADJ DAG data struction creation time:", DS_ADJ)
if DS_Tree>0:
    print("Tree data struction creation time:", DS_Tree)
if DS_SV>0:
    print("smart validator verification time:", DS_SV)
        
#print('Number : ',n)
print('Execution Time : ',total)
os.remove('timing_computation.txt')


    




