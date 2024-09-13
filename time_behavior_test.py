# time_behavior_test.py

import requests
import time

SERVER_URL = 'http://127.0.0.1:5000'

def measure_message_delivery_time():
    # Send a message
    message = {'text': 'Test message for time behavior'}

    # Record the start time
    start_time = time.time()

    # Send the POST request to send the message
    response = requests.post(f"{SERVER_URL}/messages", json=message)

    if response.status_code != 201:
        print("Error sending message.")
        return

    # Poll the server until the message appears in the messages list
    max_wait_time = 5  # seconds
    poll_interval = 0.1  # seconds
    elapsed_time = 0

    while elapsed_time < max_wait_time:
        # Fetch all messages
        messages_response = requests.get(f"{SERVER_URL}/messages")
        if messages_response.status_code == 200:
            messages = messages_response.json()
            # Check if our message is in the list
            if any(msg['text'] == message['text'] for msg in messages):
                # Record the end time
                end_time = time.time()
                delivery_time = end_time - start_time
                print(f"Message delivery time: {delivery_time:.4f} seconds")
                return delivery_time
        time.sleep(poll_interval)
        elapsed_time += poll_interval

    print("Message not delivered within the maximum wait time.")
    return None

if __name__ == '__main__':
    measure_message_delivery_time()
