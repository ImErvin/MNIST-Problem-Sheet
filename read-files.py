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

i = 0

f = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')
try:
    byte = f.read(0)
    for i in range(4):
        byte = f.read(4)
        print (int.from_bytes(byte, byteorder="big"))
    for k in range(6000):
        for i in range(784):
            i = i + 1
            # Do stuff with byte.
            byte = f.read(1)
            if(int.from_bytes(byte, byteorder="big") > 0):
                print("#", end=" ")
            else:
                print(".", end=" ")
            
            # print (int.from_bytes(byte, byteorder="big"))
            if(i % 28 == 0):
                print("\n")
finally:
    f.close()