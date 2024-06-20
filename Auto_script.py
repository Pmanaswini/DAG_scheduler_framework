import subprocess
import time
import os

# Function to run a command in a new terminal
def run_in_terminal(command, terminal="gnome-terminal"):
    subprocess.run([terminal, '--', 'bash', '-c', command])

# Commands to run in each terminal
commands = {
    "terminal_1": "docker-compose up",
    "terminal_2": """
        docker exec -it sawtooth-shell-local bash -c '
        sawtooth keygen client;
        cd pyclient;
        python3 script.py'
    """,
    "terminal_3": """
        docker exec -it sawtooth-shell-local bash -c '
        cd pyprocessor;
        ./simple_wallet'
    """
}

# Open the first terminal and run docker-compose up
run_in_terminal(commands["terminal_1"])

# Delay to allow the first command to initiate
time.sleep(5)

# Open the second terminal and execute the required commands
run_in_terminal(commands["terminal_2"])

# Open the third terminal and execute the required commands
run_in_terminal(commands["terminal_3"])

# Delay to allow processes to complete as needed (customize as needed)
time.sleep(120)  # Example delay; adjust based on your process duration

# Bring down the docker-compose setup
subprocess.run("docker-compose down", shell=True)
