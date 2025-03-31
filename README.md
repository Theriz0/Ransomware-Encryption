# Ransomware Simulation (Educational Purposes Only)

This project is a simple Python ransomware simulation designed for educational purposes. It demonstrates the basic concepts of file encryption and decryption using the `cryptography` library.

**Disclaimer:**

This code should only be used for educational purposes in a controlled environment. Do not use this code on systems without explicit permission. Misuse of this code can have serious consequences.

**How it Works:**

The project consists of two Python scripts:

* **`encrypt.py`:**
    * Finds all files in the current directory (excluding `main.py`, `test.key`, and `decrypt.py`).
    * Generates a Fernet encryption key.
    * Saves the key to a file named `test.key`.
    * Encrypts all found files using the generated key.
    * Prints a message simulating a ransomware demand.
* **`decrypt.py`:**
    * Finds all encrypted files in the current directory.
    * Prompts the user to enter a secret phrase.
    * If the phrase is correct, decrypts the files using the key from `test.key`.
    * Prints a success message or an error message.

**Usage:**

1.  **Clone the repository:**
    ```bash
    git clone [repository URL]
    cd Ransomware-Simulation
    ```
2.  **Install the `cryptography` library:**
    ```bash
    pip install cryptography
    ```
3.  **Run `encrypt.py`:**
    ```bash
    python encrypt.py
    ```
4.  **Run `decrypt.py`:**
    ```bash
    python decrypt.py
    ```
5.  Enter the password "1234" to test fail case of decryption for the files.
6.  Enter the exact keyphrase in decrypt.py to decrypt the files.

**Key Concepts:**

* **File Encryption:** The process of converting data into an unreadable format.
* **Decryption:** The process of converting encrypted data back into its original format.
* **Fernet:** A symmetric encryption library in Python.
* **Encryption Key:** A secret value used to encrypt and decrypt data.

**Ethical Considerations:**

* This project is for educational purposes only.
* Do not use this code to harm or disrupt any systems.
* Always obtain explicit permission before running this code on any system.
* Be aware of the legal consequences of unauthorized file encryption.
* Never pay a ransom to a real ransomware attacker.

**Improvements:**

* Add error handling.
* Use a more secure key storage mechanism.
* Implement asymmetric encryption.
* Add a GUI.
* Add logging.
* Add command line arguments.
* Use a more complex password.

**Credit:**

This project is inspired by educational content available online.
credit: https://www.youtube.com/watch?v=UtMMjXOlRQc
