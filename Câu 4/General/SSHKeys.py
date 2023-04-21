from Crypto.PublicKey import RSA

f = open("RSA.pem", "r")
key = f.read()
enc = RSA.importKey(key)
print(enc.n)