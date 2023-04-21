from pwn import *
import json
from sympy import *
from decrypt import *

r = remote('socket.cryptohack.org', 13379, level = 'debug')

def json_recv(text_to_remove):
    line = r.recvline().decode()
    for i in text_to_remove:
        line = line.strip(i)
    return json.loads(line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv(["Intercepted from Alice: "])

received["supported"] = ["DH64"]
json_send(received)

received = json_recv(["Send to Bob: ", "Intercepted from Bob: "])

json_send(received)

received = json_recv(["Send to Alice: ", "Intercepted from Alice: "])

p = int(received["p"], 16)
g = int(received["g"], 16)
A = int(received["A"], 16)
a = discrete_log(p, A, g)

received = json_recv(["Intercepted from Bob: "])

B = int(received["B"], 16)

received = json_recv(["Intercepted from Alice: "])

shared_secret = pow(B, a, p)
iv = received["iv"]
ciphertext = received["encrypted_flag"]

print(decrypt_flag(shared_secret, iv, ciphertext))