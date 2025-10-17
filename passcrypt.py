#!/usr/bin/env python3
# PassCrypt v2.0 - Main Executable
# A secure, local password encryption tool using modern cryptography.

import argparse
from passcrypt_lib import ui, crypto_logic

def handle_encrypt():
    """Workflow for encrypting credentials."""
    try:
        # 1. Get credentials from user
        credentials = ui.get_credentials_to_encrypt()
        if not credentials:
            return # User cancelled or provided empty password

        # 2. Get master password securely
        master_password = ui.get_master_password(confirm=True)
        if not master_password:
            return # User cancelled or passwords didn't match

        ui.console.print("\n[bold cyan]Encrypting data...[/bold cyan] ⏳")
        
        # 3. Perform encryption
        encrypted_blob = crypto_logic.encrypt_data(master_password, credentials)

        # 4. Display the result
        ui.display_encrypted_blob(encrypted_blob)

    except (ValueError, Exception) as e:
        ui.display_error(str(e))

def handle_decrypt():
    """Workflow for decrypting a blob."""
    try:
        # 1. Get the encrypted blob from the user
        encrypted_blob = ui.get_encrypted_blob_from_user()
        if not encrypted_blob:
            ui.display_error("Encrypted blob cannot be empty.")
            return

        # 2. Get master password securely (no confirmation needed)
        master_password = ui.get_master_password(confirm=False)
        if not master_password:
            return # User cancelled

        ui.console.print("\n[bold cyan]Decrypting data...[/bold cyan] ⏳")

        # 3. Perform decryption
        decrypted_data = crypto_logic.decrypt_data(master_password, encrypted_blob)

        # 4. Display the results in a table
        ui.display_decrypted_credentials(decrypted_data)

    except (ValueError, Exception) as e:
        # Crypto logic raises ValueError on failure, which is caught here.
        ui.display_error(str(e))


def main():
    """Main function to run the interactive tool."""
    ui.print_header()
    while True:
        choice = ui.display_main_menu()
        if choice == '1':
            handle_encrypt()
        elif choice == '2':
            handle_decrypt()
        elif choice == '3':
            ui.console.print("\n[bold cyan]Goodbye![/bold cyan] 👋\n")
            break
        ui.console.print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
