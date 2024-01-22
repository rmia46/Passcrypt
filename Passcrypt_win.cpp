// libs
#include <iostream>
#include <string.h>
#include <cmath>
#include <string>
#include <time.h>
#include <cstdlib>

// colors
// const std::string red("\033[1;31m");
// const std::string green("\033[1;32m");
// const std::string yellow("\033[1;33m");
// const std::string cyan("\033[1;36m");
// const std::string magenta("\033[0;35m");
// const std::string reset("\033[0m");

using namespace std;


// Key Generator

int getNewKey(int key)
{
    int const multiplier = 2047;

    //srand(time(0));
    int keygen = (multiplier * key) % 10000;
    if(keygen >= 9800)
        keygen -= 250;
    if(keygen <= 1000)
        keygen += 1000;
    return keygen;
}

// Encryption 

void encrypt(string pass, int key)
{
    int newkey;
    newkey = getNewKey(key);
    cout << "\nPassword encrypted with key: " << key << endl << "Code: ";
    for(int i = 0, k = 1, j = newkey; i < pass.size(); i++, k++, j = getNewKey(key+k)) {
       cout << int(pass[i]) + j;
       if(j > 900000)
           k = 1;
    }
    cout << endl;
}

// Decryption

void decrypt(string eCode, int key)
{
    int code = 0;
    int newkey = getNewKey(key);
    string subCode;
    cout << "\nPassword decrypted with key: " << key << endl << "Password: ";
    for(int i = 0, k = 1, j = newkey; i <= eCode.size()- 4; i+=4, k++, j = getNewKey(key+k)) {
        subCode = eCode.substr(i, 4);
        code = stoi(subCode);
        cout << char(code - j);
        if(j > 900000) 
           k = 1;
    }
    cout << endl;

}

// Intro Message 
void introMessage() {
	cout << "\n    .-\"\"-. " << endl << "   / .--. \\ " << endl << "  / /    \\ \\ "<< endl << "  | |    | | " << endl << "  | |.-\"\"-.| " << endl << " ///`.::::.`\\ " << endl << "||  ::/  \\:: ; " << endl << "||; ::\\__/:: ; " << endl << " \\\\\\ '::::' / " << endl << "  `=':-..-'` " << endl;
	cout << "Passcrypt v1.1\n";
    cout << "Dev:" << " RMia\n";
}

// Chagelog
void changelog()
{
	cout << "\nPasscrypt version 1.1\nDeveloper: Roman\n";
	cout << "Changelog v1.0\n";
        cout << "-Added colors." << endl;
        cout << "-Fixed a major bug!." << endl;
        cout << "Changelog v1.1\n";
        cout << "-Fixed some bugs!." << endl;
        cout << "-Encryption algorithm updated!\n";
        cout << "Report any bug to- " << "blindhawk46@gmail.com\n";
}	


// Driver Program
void choice()
{
    cout << "\nAvailable options:" << endl;
    cout << "1. Encrypt" << endl;
    cout << "2. Decrypt" << endl;
    cout << "3. Clear Screen" << endl;
    cout << "4. About" << endl;
    cout << "5. Exit" << endl;
    // user input
    int input, key;
    string password, code;
    cout << "=> ";
    cin >> input;
    if ( !cin ) {
        cout << "Bad input" << endl;
        cin.clear();
        cin.ignore();
        system("clear");
        cout  << "Bad Input! Program Restarted.\n";
        choice();
        }
    if(input == 1) {
        cout << "Enter the pass: ";
        getline(cin >> ws, password);
        
        cout << "Enter a key" << " (Must be a 5 digit number): ";
        cin >> key;
        if ( !cin ) {
        cout << "Bad input" << endl;
        cin.clear();
        cin.ignore();
        system("clear");
        cout << "Bad Input! Program Restarted.\n";
        choice();
        }
        cout << "Must remember the key!!\n" << endl;
        encrypt(password, key);
        choice();
    }
    else if(input == 2) {
        cout  << "Enter encrypted code: ";
        cin >> code;
        cout << "Enter the key (Forgot? Go cry to your Mama): ";
        cin >> key;
        if ( !cin ) {
        cout << "Bad input" << endl;
        cin.clear();
        cin.ignore();
        system("clear");
        cout << "Bad Input! Program Restarted.\n";
        choice();
        }
        decrypt(code, key);
        choice();
    }
    else if(input == 3) {
       // cout << string(70, '\n');
       // Windows
       //system("cls");
       // Linux
       system("clear");
       introMessage();
       choice();
    }
    else if(input == 4) {
        changelog();
        choice();
        }
    else if(input == 5) {
    	cout << "Program Terminated\n";
        exit(0);
    }

    else {
        cout << "Wrong Input!\n";
        choice();
    
    }
}

// Main Function
int main()
{
    // intro
    introMessage();

    choice();

    return 0;
}
