from pwn import * # pip install pwntools
import json
from decrypt import *

r = remote('socket.cryptohack.org', 13380, level = 'debug')

def json_recv(text_to_remove):
    line = r.recvline().decode()
    for i in text_to_remove:
        line = line.strip(i)
    return json.loads(line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv(["Intercepted from Alice: "])

p = int(received["p"], 16)
g = int(received["g"], 16)
A = int(received["A"], 16)
a = A * pow(g, -1, p)

received = json_recv(["Intercepted from Bob: "])

B = int(received["B"], 16)

receive = json_recv(["Intercepted from Alice: "])

shared_secret = B * a % p
iv = receive["iv"]
ciphertext = receive["encrypted"]

print(decrypt_flag(shared_secret, iv, ciphertext))