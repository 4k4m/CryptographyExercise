import json

from Crypto.Util.number import bytes_to_long, long_to_bytes

from pwn import *

p1 = 211578328037

p2 = 2173767566209

conn = remote('socket.cryptohack.org', 13376)

data = conn.recvline()

resp = dict()

resp['option'] = 'get_pubkey'

conn.send(json.dumps(resp))

data = json.loads(conn.recvline())

N = bytes_to_long(bytes.fromhex(data['N'][2:]))

resp = dict()

resp['option'] = 'sign'

resp['msg'] = long_to_bytes(p1).hex()

conn.send(json.dumps(resp))

data = json.loads(conn.recvline())

s1 = bytes_to_long(bytes.fromhex(data['signature'][2:]))

resp = dict()

resp['option'] = 'sign'

resp['msg'] = long_to_bytes(p2).hex()

conn.send(json.dumps(resp))

data = json.loads(conn.recvline())

s2 = bytes_to_long(bytes.fromhex(data['signature'][2:]))

signature = (s1 * s2) % N

resp = dict()

resp['option'] = 'verify'

resp['msg'] = b'admin=True'.hex()

resp['signature'] = long_to_bytes(signature).hex()

conn.send(json.dumps(resp))

data = json.loads(conn.recvline())

print(data['response'])
