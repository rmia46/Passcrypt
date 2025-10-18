# passcrypt_lib/ui.py
# Manages all user interface elements using the 'rich' library.

import getpass
import pyperclip
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.text import Text

# Initialize a global console object
console = Console()

def print_header():
    """Prints the application header."""
    header_text = Text("PassCrypt v2.1.0", style="bold magenta", justify="center")
    sub_header = Text("Secure Local Password Encryption Tool", style="cyan", justify="center")
    credits_text = Text("by Gemini, in association with @rmia46", style="dim", justify="center")
    
    console.print(Panel.fit(
        Text("\n").join([header_text, sub_header, credits_text]),
        title="[bold green]Welcome[/bold green]",
        border_style="green"
    ))
    console.print()

def get_master_password(confirm: bool = True) -> str:
    """Securely prompts the user for a master password."""
    console.print("[bold yellow]🔑 Enter Master Key[/bold yellow]")
    try:
        password = getpass.getpass("   > ")
        if confirm:
            password_confirm = getpass.getpass("   Confirm > ")
            if password != password_confirm:
                console.print("[bold red]Error: Passwords do not match.[/bold red]")
                return None
        if not password:
            console.print("[bold red]Error: Master key cannot be empty.[/bold red]")
            return None
        return password
    except Exception as e:
        console.print(f"[bold red]Error reading password: {e}[/bold red]")
        return None

def get_credentials_to_encrypt() -> dict:
    """Prompts the user for the credentials they want to encrypt."""
    console.print(Panel(
        "[cyan]Enter the details to encrypt. You can leave any field blank.",
        title="[bold green]Encryption Details[/bold green]",
        border_style="cyan"
    ))
    email = Prompt.ask("   📧 [bold]Email[/bold]", default="", show_default=False)
    username = Prompt.ask("   👤 [bold]Username[/bold]", default="", show_default=False)
    password = Prompt.ask("   🔒 [bold]Password[/bold]", password=False) # password=True hides input
    
    if not password:
        console.print("[bold red]Error: The password field cannot be empty.[/bold red]")
        return None

    return {"email": email, "username": username, "password": password}

def get_encrypted_blob_from_user() -> str:
    """Prompts the user to paste the encrypted data blob."""
    console.print(Panel(
        "Paste the entire encrypted string below and press Enter.",
        title="[bold yellow]Decrypt Data[/bold yellow]",
        border_style="yellow"
    ))
    blob = Prompt.ask("   [bold]Encrypted Blob[/bold]")
    return blob.strip()

def display_decrypted_credentials(credentials: dict):
    """Displays the decrypted credentials in a clean table."""
    table = Table(title="🔓 Decrypted Credentials", show_header=True, header_style="bold green", border_style="green")
    table.add_column("Field", style="dim", width=12)
    table.add_column("Value", style="bold")

    table.add_row("Email", credentials.get("email", "N/A"))
    table.add_row("Username", credentials.get("username", "N/A"))
    
    password = credentials.get("password", "[red]ERROR[/red]")
    table.add_row("Password", password)

    console.print(table)

    if password != "[red]ERROR[/red]" and Confirm.ask("\n[bold yellow]📋 Copy password to clipboard?[/bold yellow]"):
        try:
            pyperclip.copy(password)
            console.print("[bold green]Password copied to clipboard![/bold green]")
        except pyperclip.PyperclipException as e:
            console.print(f"[bold red]Error: Could not copy to clipboard. {e}[/bold red]")

def display_encrypted_blob(blob: str):
    """Displays the final encrypted blob for the user to copy."""
    console.print(Panel(
        "[bold green]✅ Encryption Successful[/bold green]",
        border_style="green",
        expand=False
    ))
    console.print("\n[bold cyan]Your encrypted data blob is:[/bold cyan]")
    console.print(blob)
    
    if Confirm.ask("\n[bold yellow]📋 Copy to clipboard?[/bold yellow]"):
        try:
            pyperclip.copy(blob)
            console.print("[bold green]Copied to clipboard![/bold green]")
        except pyperclip.PyperclipException as e:
            console.print(f"[bold red]Error: Could not copy to clipboard. {e}[/bold red]")
            console.print("You can still copy the blob manually from the console.")

def display_error(message: str):
    """Displays an error message in a styled panel."""
    console.print(Panel(
        f"[bold red]{message}[/bold red]",
        title="[bold red]❌ Error[/bold red]",
        border_style="red"
    ))

def display_main_menu() -> str:
    """Displays the main menu and returns the user's choice."""
    console.print(Panel(
        "[bold green]1.[/bold green] Encrypt Credentials\n"
        "[bold yellow]2.[/bold yellow] Decrypt Credentials\n"
        "[bold red]3.[/bold red] Exit",
        title="[bold cyan]Main Menu[/bold cyan]",
        border_style="cyan"
    ))
    choice = Prompt.ask("   Enter your choice [1-3]", choices=["1", "2", "3"], show_choices=False)
    return choice
