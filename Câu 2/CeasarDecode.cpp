#include <iostream>
#include <string>
using namespace std;

string ceasarDecode(string &str, int key) {
	string result;

    for (char i: str) {
        if (i >= 'a' && i <= 'z') {
            result.push_back((i + key) - (i + key > 'z'? 26: 0)); 
            continue;
        }

        if (i >= 'A' && i <= 'Z') {
            result.push_back((i + key) - (i + key > 'Z'? 26: 0));
            continue;
        }

        result.push_back(i);
    }
    
    return result;
}

int main() {
	string str;
	cout << "Ciphertext: ";
	getline(cin, str);
	int key;
    cout << "Possible plaintexts:\n";
	for (int key = 1; key < 26; key++) {
	    string plaintext = ceasarDecode(str, key);
        cout << plaintext << '\n';
    }
	return 0;
}