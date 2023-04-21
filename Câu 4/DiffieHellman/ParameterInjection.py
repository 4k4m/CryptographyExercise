from pwn import * # pip install pwntools
import json
from decrypt import *

r = remote('socket.cryptohack.org', 13371, level = 'debug')

def json_recv(text_to_remove):
    line = r.recvline().decode()
    for i in text_to_remove:
        line = line.strip(i)
    return json.loads(line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv(["Intercepted from Alice: "])

p = received["p"]
received["A"] = received["p"]

json_send(received)

received = json_recv(["Send to Bob: ", "Intercepted from Bob: "])

received["B"] = str(p)

json_send(received)

receive = json_recv(["Send to Alice: ", "Intercepted from Alice: "])

shared_secret = 0
iv = receive["iv"]
ciphertext = receive["encrypted_flag"]

print(decrypt_flag(shared_secret, iv, ciphertext))