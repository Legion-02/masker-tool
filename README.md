# 🔐 Masker

### Lightweight CLI Hashing & Verification Utility

> A professional command-line tool for generating and verifying
> cryptographic hashes using Python's built-in hashlib library.

------------------------------------------------------------------------

## 🚀 Overview

**Masker** is a lightweight CLI-based hashing utility designed to:

-   🔑 Generate cryptographic hashes
-   ✅ Verify text against existing hashes
-   🖥️ Provide a structured command-line interface
-   🧩 Demonstrate applied cryptographic fundamentals

This project showcases practical understanding of cryptographic hashing,
CLI architecture, and secure coding practices using Python standard
libraries.

------------------------------------------------------------------------

## ✨ Features

### 🔒 Hash Generation

Supports algorithms available in Python's `hashlib`, including:

-   MD5
-   SHA1
-   SHA256
-   SHA512
-   Any algorithm supported by your Python installation

### ✅ Hash Verification

Compare plaintext input against a known hash to validate integrity.

------------------------------------------------------------------------

## 🖥️ Output Examples

### 1️⃣ Generate SHA256 Hash

Command:

``` bash
python masker.py hash sha256 password123
```

Output:

    ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f

------------------------------------------------------------------------

### 2️⃣ Generate SHA512 Hash

Command:

``` bash
python masker.py hash sha512 SecurePass!
```

Output:

    0e3397b4abc7a382b3ea2365883c3c7ca5f5c4f0bb9d8a9b77d8a6e7f0e92ce40938e425c205b5b61896f8aeecc65c1dcaf149048393ca5c7d07212e7260213f

------------------------------------------------------------------------

### 3️⃣ Verify Hash (Correct Match)

Command:

``` bash
python masker.py verify sha256 password123 ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```

Output:

    Match

------------------------------------------------------------------------

### 4️⃣ Verify Hash (Incorrect Match)

Command:

``` bash
python masker.py verify sha256 password123 abc123
```

Output:

    No Match

------------------------------------------------------------------------

## 🛠️ Installation

``` bash
git clone https://github.com/yourusername/masker.git
cd masker
python masker.py -h
```

------------------------------------------------------------------------

## 📦 Requirements

This project uses only Python standard libraries:

-   hashlib
-   argparse
-   sys

✅ No external dependencies required\
🐍 Tested on Python 3.8+

------------------------------------------------------------------------

## 🧠 Technical Highlights

-   Use of Python's `hashlib` for cryptographic hashing
-   CLI argument parsing with `argparse`
-   Subcommand-based CLI architecture
-   Hash comparison logic for verification
-   Clean, modular, and extensible code design

------------------------------------------------------------------------

## 🔐 Security Notes

-   MD5 and SHA1 are included for educational purposes.
-   For secure applications, SHA256 or stronger algorithms are
    recommended.
-   Intended for learning, lab environments, and authorized use only.

------------------------------------------------------------------------

## 🎯 Why This Project Matters

Masker demonstrates:

-   Understanding of cryptographic primitives
-   Secure password handling concepts
-   CLI tool development skills
-   Practical implementation of hash verification workflows

------------------------------------------------------------------------

## ⚠️ Disclaimer

This tool is intended for educational and authorized security testing
purposes only.

------------------------------------------------------------------------

## 👨‍💻 Author

**Anush**\
Cyber Security Enthusiast
