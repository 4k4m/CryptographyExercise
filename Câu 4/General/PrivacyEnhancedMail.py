from Crypto.PublicKey import RSA

f = open("privacy_enhanced_mail.pem", "r")
key = f.read()
enc = RSA.importKey(key)
print(enc.d)