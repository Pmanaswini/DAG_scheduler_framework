import subprocess
import time

# Function to run a command in a new tmux session
def run_in_tmux(session_name, command):
    subprocess.run(['tmux', 'new-session', '-d', '-s', session_name, command])

# Commands to run in each tmux session
commands = {
    "session_1": "docker-compose up",
    "session_2": """
        docker exec -it sawtooth-shell-local bash -c '
        sawtooth keygen client;
        cd pyclient;
        python3 script.py'
    """,
    "session_3": """
        docker exec -it sawtooth-shell-local bash -c '
        cd pyprocessor;
        ./simple_wallet'
    """
}

# Open the first tmux session and run docker-compose up
run_in_tmux("session_1", commands["session_1"])

# Delay to allow the first command to initiate
time.sleep(5)

# Open the second tmux session and execute the required commands
run_in_tmux("session_2", commands["session_2"])

# Open the third tmux session and execute the required commands
run_in_tmux("session_3", commands["session_3"])

# Delay to allow processes to complete as needed (customize as needed)
time.sleep(120)  # Example delay; adjust based on your process duration

# Bring down the docker-compose setup
subprocess.run("docker-compose down", shell=True)
