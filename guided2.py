# Caesar Cipher

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {}

# Automatically generate the decode table from the encode table
for k, v in encode_table.items():
  decode_table[v] = k


def encode(s):
  r = ""
  for c in s:
    r += encode_table[c]
  return r


def decode(s):
  r = ""
  for c in s:
    r += decode_table[c]
  return r


print(encode("BEEJ")) # plain text
print(decode("ZOOT")) # cypher text



import hashlib
import random


def hash_function(key):
  return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16)&0xffffffff


def how_many_before_collision(buckets, loops=1):
  for i in range(loops):
    tries = 0
    tried = set()

    while True:
      random_key = random.random()
      index = hash_function(random_key) % buckets

      if index not in tried:
        tried.add(index)
        tries += 1
      else:
        break

    print(f'{buckets}, {tries} before collision. ')










