import os
import time
import subprocess
import re

def run_with_gap(command, gap, repetitions=2):
    for _ in range(repetitions):
        subprocess.run(command, shell=True)
        time.sleep(gap)
     #   f1=open("DAG_results_tracing.txt",a)
      #  f1.write("command" + str(command)+ "repetitions = " + str(repetitions))
      #  f1.close()

if __name__ == "__main__":
    # Copy keys with 1 min gap
    command= "cp -r /project/sawtooth-core/keys /root/.sawtooth"
    subprocess.run(command, shell=True)
    time.sleep(10)
    # Run simplewallet init.txt with 1 min gap
    command= "./simplewallet init.txt"
    #run_with_gap("./simplewallet init.txt", 100)
    subprocess.run(command, shell=True)
    time.sleep(90)
     Run simplewallet 200.txt with 1 min gap
    run_with_gap("./simplewallet 200.txt", 10)
    run_with_gap("./simplewallet 400.txt", 10)
    run_with_gap("./simplewallet 600.txt", 20)
    run_with_gap("./simplewallet 800.txt", 30)        
    run_with_gap("./simplewallet 1000.txt", 50)
    run_with_gap("./simplewallet 1200.txt", 50)
    run_with_gap("./simplewallet 1400.txt", 90)            
    run_with_gap("./simplewallet 1600.txt", 90)    
    run_with_gap("./simplewallet 1800.txt", 110)    
    run_with_gap("./simplewallet 2000.txt", 100)    
