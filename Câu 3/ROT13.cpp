#include <iostream>
#include <string>

using namespace std;

// to encrypt or decrypt a message using ROT13 algorithm
string encryptDecryptROT13(string &text) {
    string result; // resulting text

    // replace each letter by 13th letter on
    for (char i: text) {
        if (i >= 'a' && i <= 'z') { // lowercase letters
            result.push_back((i + 13) - (i + 13 > 'z'? 26: 0)); 
            continue;
        }

        if (i >= 'A' && i <= 'Z') { // uppercase letters
            result.push_back((i + 13) - (i + 13 > 'Z'? 26: 0));
            continue;
        }

        result.push_back(i); // other characters
    }
    
    return result;
}

int main() {
    string originalText; // originalText may be a plaintext or a ciphertext
    cout << "Original Text: "; // ask user to input originalText
    getline(cin, originalText); // read originalText
    cout << "Text after encryption/decryption: " << encryptDecryptROT13(originalText); // print the resulting text
    return 0;
}