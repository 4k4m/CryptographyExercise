from pwn import * # pip install pwntools
import json
from Crypto.Util.number import *
from decrypt import *
from sympy import *

r = remote('socket.cryptohack.org', 13378, level = 'debug')

def json_recv(text_to_remove):
    line = r.recvline().decode()
    print(line)
    for i in text_to_remove:
        line = line.strip(i)
    return json.loads(line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def generate_smooth_prime(bitlen):
    p = 2
    while p.bit_length() <= bitlen:
        q = getPrime(20)
        p *= q
    while True:
        q = getPrime(20)
        if isPrime(p * q + 1):
            p = p * q + 1
            return p


received = json_recv(["Intercepted from Alice: "])

p = int(received["p"], 16)
bitlen = p.bit_length()
my_p = generate_smooth_prime(bitlen)
A = int(received["A"], 16)

received = json_recv(["Intercepted from Bob: "])

B = received["B"]

received = json_recv(["Intercepted from Alice: "])

iv = received["iv"]
ciphertext = received["encrypted"]

json_send({"p": hex(my_p), "g": hex(2), "A": hex(A)})

received = json_recv(["Bob connects to you, send him some parameters: ", "Bob says to you: "])

B = int(received["B"], 16)
b = discrete_log(my_p, B, 2)

shared_secret = pow(A, b, p)

print(decrypt_flag(shared_secret, iv, ciphertext))