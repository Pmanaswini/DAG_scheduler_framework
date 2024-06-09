import os
import time
import subprocess
import re

def run_with_gap(command, gap, repetitions=1):
    for _ in range(repetitions):
        subprocess.run(command, shell=True)
        time.sleep(gap)

if __name__ == "__main__":
    # Copy keys with 1 min gap
    command= "cp -r /project/sawtooth-core/keys /root/.sawtooth"
    subprocess.run(command, shell=True)
    time.sleep(20)
    # Run simplewallet init.txt with 1 min gap
    command= "./simplewallet init.txt"
    subprocess.run(command, shell=True)
    time.sleep(60)
    # Run simplewallet 200.txt with 1 min gap
    run_with_gap("./simplewallet 200.txt", 10)
    run_with_gap("./simplewallet 400.txt", 10)
    run_with_gap("./simplewallet 600.txt", 20)
    run_with_gap("./simplewallet 800.txt", 20)        
    run_with_gap("./simplewallet 1000.txt", 40)
    run_with_gap("./simplewallet 1200.txt", 40)
    run_with_gap("./simplewallet 1400.txt", 80)            
    run_with_gap("./simplewallet 1600.txt", 80)    
    run_with_gap("./simplewallet 1800.txt", 100)    
    run_with_gap("./simplewallet 2000.txt", 100)    
