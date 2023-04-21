from pwn import * # pip install pwntools
import json
import base64
from Crypto.Util.number import bytes_to_long, long_to_bytes
import codecs


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):
    received = json_recv()
    decoded = ""
    if (received["type"] == "base64"):
        decoded = base64.b64decode(received["encoded"]).decode()
    elif (received["type"] == "hex"):
        decoded = bytes.fromhex(received["encoded"]).decode()
    elif (received["type"] == "rot13"):
        decoded = codecs.decode(received["encoded"], "rot13")
    elif (received["type"] == "bigint"):
        decoded = long_to_bytes(int(received["encoded"], 0)).decode()
    elif (received["type"] == "utf-8"):
        decoded = "".join([chr(i) for i in received["encoded"]])

    to_send = {
        "decoded": decoded
    }

    json_send(to_send)

json_recv()
