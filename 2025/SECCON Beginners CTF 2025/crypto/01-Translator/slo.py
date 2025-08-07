from pwn import *
from Crypto.Util.number import *

p = remote("01-translator.challenges.beginners.seccon.jp", 9999)

p.sendlineafter("translations for 0>", "A"*16)
p.sendlineafter("translations for 1>", "B"*16)

p.recvuntil("ct: ")
ct = p.recvline().strip().decode()
raw = bytes.fromhex(ct)
blocks = [raw[i:i+16] for i in range(0, len(raw), 16)][:-1]

# 先頭ビットは1
one = blocks[0]
bits = ["1" if b == one else "0" for b in blocks]
bitstr = "".join(bits)

print(long_to_bytes(int(bitstr, 2)))