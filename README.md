# Encrypted Chat Application (AES Secure Messaging)

This project is a secure client/server chat application built in Python.  
It demonstrates encrypted communication using AES symmetric encryption, socket programming, and multi-client support.

The goal of this project is to understand how encrypted messaging works in real-world systems and to practice secure software design.

---

## Features

- AES encrypted messages using Fernet (cryptography library)
- TCP client/server architecture
- Multi-client support with threading
- Secure key handling with pre-shared key model
- Message logging (encrypted logs)
- Error handling and connection management
- Works across machines on local or remote networks

---

## How It Works

1. Client encrypts messages using AES
2. Encrypted data is sent to the server
3. Server relays encrypted messages to other clients
4. Clients decrypt messages locally

The server never sees plaintext messages — only encrypted data.

This design simulates real-world secure messaging systems.

---

## Requirements

Python 3.9+

Install dependencies:

