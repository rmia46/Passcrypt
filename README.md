# PassCrypt: A Secure Local Password Encryption Tool

PassCrypt is a simple yet powerful command-line tool for securely encrypting and decrypting sensitive information, such as passwords and API keys, directly on your local machine. It uses modern, robust cryptographic libraries to ensure your data remains safe.

This project was developed with the assistance of **Gemini**, a large language model from Google, who provided the code, explanations, and features.

## Features

*   **Strong Encryption:** Utilizes AES-256-GCM for authenticated encryption, providing both confidentiality and integrity.
*   **Secure Key Derivation:** Employs Scrypt, a memory-hard key derivation function, to protect against brute-force attacks on your master password.
*   **Interactive CLI:** A user-friendly interactive menu for easy encryption and decryption operations.
*   **Clipboard Integration:** Conveniently copy your encrypted data blobs and decrypted passwords to the clipboard.
*   **Self-Contained:** Runs entirely on your local machine, ensuring your secrets are never transmitted over the network.

## How to Use
### You can use the prebuilt binaries from the release. 
Or if you wish to compile and run follow the instructions: 
1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application:**
    ```bash
    python3 passcrypt.py
    ```

3.  **Follow the on-screen interactive menu to encrypt or decrypt your credentials.**

## Creating a Standalone Binary

You can create a single-file executable of PassCrypt using **PyInstaller**. This allows you to run the application on any compatible machine without needing to install Python or the required dependencies.

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```

2.  **Build the Executable:**
    From the project root directory, run the following command:
    ```bash
    pyinstaller --onefile --name passcrypt passcrypt.py
    ```

3.  **Run the Binary:**
    The standalone executable will be located in the `dist` directory. You can run it directly:
    ```bash
    ./dist/passcrypt
    ```

