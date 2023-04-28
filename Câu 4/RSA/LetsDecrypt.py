from pwn import *
from json import dumps, loads
from gmpy2 import next_prime
from Crypto.Util.number import *
import pkcs1

p = int(next_prime(2^256))
q = int(next_prime(p))
N = p * q

io = remote("socket.cryptohack.org", 13391)

io.recvline()
io.sendline(dumps({"option": "get_signature"}))
sig = int(loads(io.recvline())["signature"], 16)
msg = "I am Mallory own CryptoHack.org"
digest = pkcs1.emsa_pkcs1_v15.encode(msg.encode(), 256)
# sig * sig - N = dig
N = sig - bytes_to_long(digest)
e = 1
io.sendline(dumps({"msg": msg, "N": hex(N), "e": hex(e), "option": "verify"}))
print(loads(io.recvline()))
