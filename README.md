# Anonymous Chat Application

A simple client-server chat application where users can send and receive anonymous messages. The system also provides an endpoint to retrieve the total number of messages sent. This project emphasizes measuring the quality of the system in terms of **Time Behavior**, **Recoverability**, and **Maintainability**.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [Running the Client](#running-the-client)
- [Fitness Functions](#fitness-functions)
  - [Time Behavior Fitness Function](#1-time-behavior-fitness-function)
  - [Recoverability Fitness Function](#2-recoverability-fitness-function)
  - [Maintainability Fitness Function](#3-maintainability-fitness-function)
- [Running Unit Tests and Coverage Report](#running-unit-tests-and-coverage-report)
- [Ideas for Improvement](#ideas-for-improvement)
- [Demo Video](#demo-video)
- [Repository Link](#repository-link)
- [Contact](#contact)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Project Structure

```plaintext
.
├── client.py
├── server.py
├── time_behavior_test.py
├── recoverability_test.py
├── test_server.py
├── messages.json
├── requirements.txt
└── README.md
```

- **`client.py`**: Client application code.
- **`server.py`**: Server application code.
- **`time_behavior_test.py`**: Fitness function script for Time Behavior.
- **`recoverability_test.py`**: Fitness function script for Recoverability.
- **`test_server.py`**: Unit tests for the server.
- **`messages.json`**: Data file for persistent message storage (generated at runtime).
- **`requirements.txt`**: List of Python dependencies.
- **`README.md`**: Project documentation.

---

## Features

- **Anonymous Messaging**: Send and receive messages without user authentication.
- **View Messages**: Clients can retrieve all messages from the server.
- **Message Count Endpoint**: Retrieve the total number of messages via `/messages/count`.
- **Persistent Storage**: Messages are saved to a file to ensure data is not lost on server restart.

---

## Requirements

- **Python**: Version 3.10 or higher.
- **Dependencies**: Listed in `requirements.txt`.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SergePolin/soft-arch-hw1.git
   cd soft-arch-hw1
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Server

1. **Navigate to the Project Directory**

   ```bash
   cd soft-arch-hw1
   ```

2. **Start the Server**

   ```bash
   python server.py
   ```

   - The server will start on `http://127.0.0.1:5000`.
   - Messages are stored persistently in `messages.json`.

---

## Running the Client

1. **Open a New Terminal Window**

2. **Navigate to the Project Directory**

   ```bash
   cd soft-arch-hw1
   ```

3. **Run the Client**

   ```bash
   python client.py
   ```

4. **Interact with the Application**

   - **Menu Options**:
     - `1. View all messages`
     - `2. Send a message`
     - `3. Get message count`
     - `4. Exit`

---

## Fitness Functions

### **1. Time Behavior Fitness Function**

**Objective**: Measure the response time of the server when processing and delivering messages.

**Script**: `time_behavior_test.py`

**Running the Test**:

```bash
python time_behavior_test.py
```

**Sample Output**:

```bash
Message delivery time: 0.3521 seconds
```

**Explanation**:

- The script sends a message and measures the time until the message is confirmed to be in the server's message list.
- Adjust `max_wait_time` and `poll_interval` in the script if necessary.

### **2. Recoverability Fitness Function**

**Objective**: Test the system's ability to recover from a server crash and restore its previous state.

**Script**: `recoverability_test.py`

**Running the Test**:

```plaintext
python recoverability_test.py
```

**Sample Output**:

```plaintext
127.0.0.1 - - [Date Time] "POST /messages HTTP/1.1" 201 -
Server crashed.
Signal 15 received, saving messages and exiting...
127.0.0.1 - - [Date Time] "GET /messages HTTP/1.1" 200 -
Server recovered in 1.05 seconds.
Messages recovered successfully.
```

**Explanation**:

- The script simulates a server crash by sending a `SIGTERM` signal to the server.
- It restarts the server and checks if the previously sent message is recovered.
- Ensure no other instances of the server are running when executing this test.
- The server must have signal handlers implemented for `SIGTERM` and `SIGINT`.

### **3. Maintainability Fitness Function**

**Objective**: Measure code quality, complexity, and test coverage.

#### **A. Code Quality with Pylint**

**Install Pylint**:

```bash
pip install pylint
```

**Run Pylint**:

```bash
pylint server.py client.py
```

**Sample Output**:

```plaintext
Your code has been rated at 9.00/10
```

**Explanation**:

- Review warnings and errors to improve the code quality score.

#### **B. Code Complexity with Radon**

**Install Radon**:

```bash
pip install radon
```

**Run Radon**:

```bash
radon cc server.py client.py -a
```

**Sample Output**:

```plaintext
server.py
    F 22:0 handle_messages - A (4)
    F 75:0 message_count - A (1)
    A 2:0 Average complexity: A (2.5)

client.py
    F 8:0 display_menu - A (1)
    F 12:0 view_messages - A (5)
    F 24:0 send_message - A (4)
    F 36:0 get_message_count - A (3)
    F 48:0 main - B (6)
    A 2:0 Average complexity: A (3.8)
```

**Explanation**:

- Aim for an average complexity of A or B.

#### **C. Test Coverage with Coverage.py**

**Unit Tests File**: `test_server.py`

**Running Unit Tests**:

```bash
python -m unittest test_server.py
```

**Sample Output**:

```plaintext
...
----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK
```

**Running Coverage Analysis**:

**Install Coverage.py**:

```bash
pip install coverage
```

**Run Tests with Coverage**:

```bash
coverage run test_server.py
```

**Generate Coverage Report**:

```bash
coverage report -m
```

**Sample Output**:

```plaintext
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
server.py        70      0   100%
-------------------------------------------
TOTAL            70      0   100%
```

---

## Running Unit Tests and Coverage Report

### **Running Unit Tests**

```bash
python -m unittest test_server.py
```

### **Running Coverage Analysis**

```bash
coverage run test_server.py
coverage report -m
```

---

## Ideas for Improvement

1. **Time Behavior Enhancements**:

   - Implement asynchronous I/O to improve response times.
   - Conduct load testing to identify and optimize bottlenecks.

2. **Recoverability Enhancements**:

   - Integrate a robust database system for data persistence.
   - Implement automated failover mechanisms for high availability.

3. **Maintainability Enhancements**:

   - Refactor code for better modularity and reusability.
   - Add comprehensive documentation and adhere to coding standards.
   - Set up Continuous Integration pipelines for automated testing.

4. **Additional Testing**:

   - Increase unit test coverage to 100%.
   - Add integration and user acceptance tests.

5. **Logging and Monitoring**:
   - Implement detailed logging for easier debugging.
   - Use monitoring tools to track application performance in real-time.

---

## Demo Video

A demo video showcasing the application and fitness functions is available at:

[Demo Video](#)

---

## Repository Link

The code repository is publicly available at:

[GitHub Repository](https://github.com/SergePolin/soft-arch-hw1)

---

## Contact

For any questions or feedback, please contact:

- **Sergei Polin, <s.polin@innopolis.university>**:
- **Eleonora Pikalova, <e.pikalo@innopolis.university>**:
- **Sergey Katkov, <s.katkov@innopolis.university>**:

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Flask**: For providing an easy-to-use web framework.
- **Python Community**: For the extensive libraries and support.
