#include <iostream>
#include <string.h>
#include <cmath>
#include <string>
#include <time.h>
#include <cstdlib>
// colors
const std::string red("\033[1;31m");
const std::string green("\033[1;32m");
const std::string yellow("\033[1;33m");
const std::string cyan("\033[1;36m");
const std::string magenta("\033[0;35m");
const std::string reset("\033[0m");

using namespace std;

int getNewKey(int key)
{
    int const masterkey = 2047;
    
    //srand(time(0));
    int keygen = (masterkey * key) % 10000;
    if(keygen >= 9800)
        keygen -= 250;
    if(keygen <= 1000)
        keygen += 1000;
    return keygen;
}
void encrypt(string pass, int key)
{
    int newkey;
    newkey = getNewKey(key);
    cout << green << "\nPassword encrypted with key: " << key << endl << "Code: " << reset;
    for(int i = 0, k = 1, j = newkey; i < pass.size(); i++, k++, j = getNewKey(key+k)) {
        cout << int(pass[i]) + j;
    }
    cout << endl;
}
void decrypt(string eCode, int key)
{
    int code = 0;
    int newkey = getNewKey(key);
    string subCode;
    cout << green << "\nPassword decrypted with key: " << key << endl << "Password: " << reset;
    for(int i = 0, k = 1, j = newkey; i <= eCode.size()- 4; i+=4, k++, j = getNewKey(key+k)) {
        subCode = eCode.substr(i, 4);
        code = stoi(subCode);
        cout << char(code - j);
    }
    cout << endl;

}
void introMessage() {
	cout << cyan << "\n    .-\"\"-. " << endl << "   / .--. \\ " << endl << "  / /    \\ \\ "<< endl << "  | |    | | " << endl << "  | |.-\"\"-.| " << endl << " ///`.::::.`\\ " << endl << "||  ::/  \\:: ; " << endl << "||; ::\\__/:: ; " << endl << " \\\\\\ '::::' / " << endl << "  `=':-..-'` " << endl << reset; 
	cout << green << "Passcrypt v1.1\n" << reset;
    cout << "Dev:" << red << " RMia\n" << reset;
}
void changelog()
{
	cout << magenta << "\nPasscrypt version 1.1\nDeveloper: Roman\n" << reset;
	cout << yellow << "Changelog v1.0\n" << reset;
        cout << "-Added colors." << endl;
        cout << "-Fixed a major bug!." << endl;
        cout << yellow << "Changelog v1.1\n" << reset;
        cout << "-Fixed some bugs!." << endl;
        cout << "-Encryption algorithm updated!\n";
        cout << "Report any bug to- " << yellow << "blindhawk46@gmail.com\n" << reset;
}	
void choice()
{
    cout << cyan << "\nAvailable options:" << endl;
    cout << "1. Encrypt" << endl;
    cout << "2. Decrypt" << endl;
    cout << "3. Clear Screen" << endl;
    cout << "4. About" << endl;
    cout << "5. Exit" << endl << reset;
    // user input
    int input, key;
    string password, code;
    cout << green << "=> " << reset;
    cin >> input;
    if ( !cin ) {
        cout << red << "Bad input" << endl << reset;
        cin.clear();
        cin.ignore();
        system("clear");
        cout << red << "Bad Input! Program Restarted.\n" << reset;
        choice();
        }
    if(input == 1) {
        cout << cyan << "Enter the pass: " << reset;
        cin >> password;
        cout << cyan << "Enter a key" << reset << magenta << " (Must be a 5 digit number)\: " << reset;
        cin >> key;
        if ( !cin ) {
        cout << red << "Bad input" << endl << reset;
        cin.clear();
        cin.ignore();
        system("clear");
        cout << red << "Bad Input! Program Restarted.\n" << reset;
        choice();
        }
        cout << yellow << "Must remember the key!!\n" << reset << endl;
        encrypt(password, key);
        choice();
    }
    else if(input == 2) {
        cout << cyan << "Enter encrypted code: " << reset;
        cin >> code;
        cout << cyan << "Enter the key (Forgot? Go cry to your Mama)\: " << reset;
        cin >> key;
        if ( !cin ) {
        cout << red << "Bad input" << endl << reset;
        cin.clear();
        cin.ignore();
        system("clear");
        cout << red << "Bad Input! Program Restarted.\n" << reset;
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
    else if(input == 5)
        exit(0);

    else {
        cout << red << "Wrong Input!\n" << reset;
        choice();
    
    }
}
int main()
{
    // intro
    introMessage();

    choice();

    return 0;
}