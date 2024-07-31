# SecureHashLoginPane

## Project Overview

This project aims to create a straightforward login pane where user passwords are securely hashed using the SHA-256 algorithm. The focus is on demonstrating how to handle passwords securely in a basic login system.

## Features

- **User Registration**: Allows users to sign up with a username and password.
- **Password Hashing**: Uses the SHA-256 algorithm to hash passwords before they are stored.
- **User Login**: Users can log in by verifying their hashed passwords against stored values.
- **Secure Storage**: Ensures that passwords are stored in a hashed format to prevent exposure of plain-text passwords.

## Implementation Details

### 1. User Registration

When a user registers, their password is hashed using SHA-256. This hashed password is then stored in the database alongside the username.

### 2. User Login

During login, the system hashes the entered password and compares it to the stored hashed password. If they match, the login is successful.

### 3. Secure Storage

Hashed passwords are securely stored in the database, ensuring that plain-text passwords are not exposed, thus enhancing security.

## Conclusion

The project illustrates how to handle user passwords securely using SHA-256 hashing. By hashing passwords before storage, the system provides a layer of protection against unauthorized access and ensures that sensitive data remains secure.
