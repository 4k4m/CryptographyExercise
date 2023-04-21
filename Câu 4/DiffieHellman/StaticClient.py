from pwn import * # pip install pwntools
import json
from decrypt import *

r = remote('socket.cryptohack.org', 13373, level = 'debug')

def json_recv(text_to_remove):
    line = r.recvline().decode()
    print(line)
    for i in text_to_remove:
        line = line.strip(i)
    return json.loads(line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv(["Intercepted from Alice: "])

p = int(received["p"], 16)
A = int(received["A"], 16)

received = json_recv(["Intercepted from Bob: "])

B = received["B"]

received = json_recv(["Intercepted from Alice: "])

iv = received["iv"]
ciphertext = received["encrypted"]

json_send({"p": hex(p), "g": hex(A), "A": "0x01"})

received = json_recv(["Bob connects to you, send him some parameters: ", "Bob says to you: "])

shared_secret = int(received["B"], 16)

print(decrypt_flag(shared_secret, iv, ciphertext))