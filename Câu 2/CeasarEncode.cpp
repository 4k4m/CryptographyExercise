#include <iostream>
#include <string>
using namespace std;

string ceasarEncode(string &str, int key) {
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
	cout << "Plaintext: ";
	getline(cin, str);
	int key;
	cout << "Shift pattern: ";
	cin >> key;
	string ciphertext = ceasarEncode(str, key);
	cout << "Ciphertext: " << ciphertext;
	return 0;
}