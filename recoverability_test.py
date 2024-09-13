# recoverability_test.py

import requests
import time
import subprocess
import os
import signal

SERVER_URL = 'http://127.0.0.1:5000'

def simulate_server_crash_and_recovery():
    # Start the server process
    server_process = subprocess.Popen(['python', 'server.py'])
    time.sleep(1)  # Wait for the server to start

    try:
        # Send a message
        message = {'text': 'Message before crash'}
        response = requests.post(f"{SERVER_URL}/messages", json=message)
        if response.status_code != 201:
            print("Error sending message before crash.")
            return

        # Simulate server crash
        os.kill(server_process.pid, signal.SIGTERM)
        print("Server crashed.")

        # Record the start time of recovery
        recovery_start_time = time.time()

        # Restart the server
        server_process = subprocess.Popen(['python', 'server.py'])
        time.sleep(1)  # Wait for the server to restart

        # Check if messages are recovered
        response = requests.get(f"{SERVER_URL}/messages")
        if response.status_code == 200:
            messages = response.json()
            if any(msg['text'] == message['text'] for msg in messages):
                recovery_end_time = time.time()
                recovery_time = recovery_end_time - recovery_start_time
                print(f"Server recovered in {recovery_time:.2f} seconds.")
                print("Messages recovered successfully.")
            else:
                print("Messages not recovered.")
        else:
            print("Error fetching messages after recovery.")

    finally:
        # Clean up: terminate the server process
        os.kill(server_process.pid, signal.SIGTERM)
        server_process.wait()
        # Remove the data file
        if os.path.exists('messages.json'):
            os.remove('messages.json')

if __name__ == '__main__':
    simulate_server_crash_and_recovery()
