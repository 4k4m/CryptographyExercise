from pwn import *
import json
import base64
from Crypto.Util.number import bytes_to_long, long_to_bytes
import codecs


r = remote('socket.cryptohack.org', 13375, level = 'debug')

def json_recv(text_to_remove):
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

r.recvline()

json_send({"option":"vote","vote":"a4c46bfb65e7eccc4e76a1ce2afc6f"})

json_recv([])
