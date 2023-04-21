from Crypto.PublicKey import RSA

f = open("CERTIFICATE.pem", "r")
key = f.read()
enc = RSA.importKey(key)
print(enc.n)