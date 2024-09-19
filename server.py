"""Server application for the Anonymous Chat Application."""

import json
import os
import sys
import signal
import atexit
from threading import RLock
from datetime import datetime

from flask import Flask, request, jsonify

app = Flask(__name__)

# File for persistent message storage
DATA_FILE = 'messages.json'

# In-memory storage for messages
messages = []
messages_lock = RLock()

def load_messages():
    """Load messages from the persistent storage file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            messages.extend(json.load(file))

def save_messages():
    """Save messages to the persistent storage file."""
    with messages_lock:
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(messages, file)

# Load messages on startup
load_messages()

# Save messages on exit
atexit.register(save_messages)

def signal_handler(sig, _frame):
    """Handle termination signals and save messages before exiting."""
    print(f'Signal {sig} received, saving messages and exiting...')
    save_messages()
    sys.exit(0)

# Register signal handlers
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

@app.route('/messages', methods=['GET', 'POST'])
def handle_messages():
    """Handle GET and POST requests for messages."""
    if request.method == 'POST':
        # Receive a new anonymous message
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Invalid message format'}), 400
        message = {
            'text': data['text'],
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        with messages_lock:
            messages.append(message)
            save_messages()
        return jsonify({'status': 'Message received'}), 201
    if request.method == 'GET':
        # Return all messages
        with messages_lock:
            return jsonify(messages), 200
    return jsonify({'error': 'Method not allowed'}), 405

@app.route('/messages/count', methods=['GET'])
def message_count():
    """Return the total count of messages."""
    with messages_lock:
        count = len(messages)
    return jsonify({'count': count}), 200

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
