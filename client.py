"""Client application for the Anonymous Chat Application."""

import requests

SERVER_URL = 'http://127.0.0.1:5000'

def display_menu():
    """Display the main menu options to the user."""
    print("\n=== Anonymous Chat Application ===")
    print("1. View all messages")
    print("2. Send a message")
    print("3. Get message count")
    print("4. Exit")

def view_messages():
    """Fetch and display all messages from the server."""
    try:
        response = requests.get(f"{SERVER_URL}/messages")
        if response.status_code == 200:
            messages = response.json()
            print("\n--- All Messages ---")
            for msg in messages:
                print(f"[{msg['timestamp']}] {msg['text']}")
        else:
            print("Error fetching messages.")
    except requests.exceptions.ConnectionError:
        print("Cannot connect to the server.")

def send_message():
    """Prompt the user to enter a message and send it to the server."""
    text = input("Enter your message: ")
    data = {'text': text}
    try:
        response = requests.post(f"{SERVER_URL}/messages", json=data)
        if response.status_code == 201:
            print("Message sent successfully.")
        else:
            print("Error sending message.")
    except requests.exceptions.ConnectionError:
        print("Cannot connect to the server.")

def get_message_count():
    """Retrieve and display the total number of messages from the server."""
    try:
        response = requests.get(f"{SERVER_URL}/messages/count")
        if response.status_code == 200:
            count = response.json()['count']
            print(f"Total messages: {count}")
        else:
            print("Error fetching message count.")
    except requests.exceptions.ConnectionError:
        print("Cannot connect to the server.")

def main():
    """Main function to run the client application."""
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == '1':
            view_messages()
        elif choice == '2':
            send_message()
        elif choice == '3':
            get_message_count()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
