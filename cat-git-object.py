import sys
import zlib
from hashlib import sha1


def main(filename):
  compressed_contents = open(filename, 'rb').read()
  decompressed_contents = zlib.decompress(compressed_contents)
  print(decompressed_contents)

  hash_value = sha1(decompressed_contents).hexdigest()
  print(hash_value)

if len(sys.argv) < 2:
  print("Usage: %s filename" % sys.argv[0])
else:
  main(sys.argv[1])
