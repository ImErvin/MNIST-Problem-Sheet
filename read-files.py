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

# i = 0

# f = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')
# try:
#     byte = f.read(0)
#     for i in range(4):
#         byte = f.read(4)
#         print (int.from_bytes(byte, byteorder="big"))
#     for k in range(6000):
#         for i in range(784):
#             i = i + 1
#             # Do stuff with byte.
#             byte = f.read(1)
#             if(int.from_bytes(byte, byteorder="big") > 0):
#                 print("#", end=" ")
#             else:
#                 print(".", end=" ")
            
#             # print (int.from_bytes(byte, byteorder="big"))
#             if(i % 28 == 0):
#                 print("\n")
# finally:
#     f.close()

# The functions (read_labels and read_images) are used to decompress, read and store a file 
# by passing the file location as a parameter.

# read_labels will parse the label files to add labels to the training/testing images.
def read_labels(file):
    try:
        with gzip.open(file) as f:
            # Should be 2049
            magic_num = int.from_bytes(f.read(4), byteorder="big")
            # Should be 60000 training file labels & 10000 testing file labels
            no_labels = int.from_bytes(f.read(4), byteorder="big")
    finally:
        f.close()

# read_images will parse the image files to 
def read_images(file):
    try:
        with gzip.open(file) as f:
            # Should be 2051
            magic_num = int.from_bytes(f.read(4), byteorder="big")
            # Should Should be 60000 training files & 10000 testing files
            no_images = int.from_bytes(f.read(4), byteorder="big")
            # Should be 28
            no_rows = int.from_bytes(f.read(4), byteorder="big")
            # Should be 28
            no_cols = int.from_bytes(f.read(4), byteorder="big")
    finally:
        f.close()