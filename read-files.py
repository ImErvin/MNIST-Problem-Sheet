# Read files written by Ervin Mamutov, github/imervin

# Adapated code from
#       https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#       https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar
#       https://stackoverflow.com/questions/1035340/reading-binary-file-and-looping-over-each-byte

import gzip

# f = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')

# initialByte = f.read(1)

# print (int.from_bytes(initialByte, byteorder="big"))

# f.close()

f = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')
try:
    byte = f.read(0)
    while byte != "":
        # Do stuff with byte.
        byte = f.read(4)
        print (int.from_bytes(byte, byteorder="big"))
finally:
    f.close()