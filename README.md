# Library Management System

A robust, CLI-based Library Management System developed in Python. This project focuses on efficient library operations, featuring user authentication, data persistence using CSV files, and input validation to ensure system stability.

## Features

- **User Authentication:** Secure login system for librarians with password verification.
- **Data Persistence:** Uses CSV files as a lightweight database to store library inventory and user credentials.
- **Automated Setup:** Automatically creates necessary CSV files if they are missing upon system startup.
- **CRUD Operations:** Create, Read, and Update functionality for the library acervo (inventory).
- **Borrowing & Returning:** Smart logic to manage book availability, preventing over-borrowing or invalid returns.
- **Input Validation:** Robust error handling that prevents system crashes and allows for easy operation cancellation via keyboard interrupts (Enter key).
- **User-Friendly Interface:** Clean, menu-driven CLI (Command Line Interface) with clear feedback for all operations.

## Project Structure

- `main.py`: The core logic of the system, handling inventory management and the main menu workflow.
- `auth.py`: Dedicated module for user authentication and staff registration.
- `acervo.csv`: Data storage for books (automatically generated).
- `usuarios.csv`: Data storage for librarian credentials (automatically generated).

## How to Run

1. Ensure you have [Python](https://www.python.org/) installed on your machine.
2. Clone this repository:
   ```bash
   git clone https://github.com/kiraDarthur/Bibliotec-rio-.git
