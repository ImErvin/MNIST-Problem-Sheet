# Read files written by Ervin Mamutov, github/imervin

# Adapated code from
#       https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#       https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar
#       https://stackoverflow.com/questions/1035340/reading-binary-file-and-looping-over-each-byte
#       https://stackoverflow.com/questions/10668341/create-3d-array-using-python

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
            # Magic number - *Expected to be 2049*
            magic_num = int.from_bytes(f.read(4), byteorder="big")
            # Number of Labels - *Expected to be 60000 training file labels & 10000 testing file labels*
            no_labels = int.from_bytes(f.read(4), byteorder="big")
            # Print out file details.
            # If parsed correctly, the values should be the same as the values expected.
            print("File:",file,"\nMagic number: \t\t%10d\nNumber of Images: \t%10d\n"%(magic_num,no_labels))
            
            label_list = [int.from_bytes(f.read(1), byteorder="big") for i in range(no_labels)]

            return label_list
    finally:
        f.close()

# read_images will parse the image files to 
def read_images(file):
    try:
        with gzip.open(file) as f:
            # *Expected to be 2051*
            magic_num = int.from_bytes(f.read(4), byteorder="big")
            # *Expected to be 60000 training files & 10000 testing files*
            no_images = int.from_bytes(f.read(4), byteorder="big")
            # *Expected to be 28*
            no_rows = int.from_bytes(f.read(4), byteorder="big")
            # *Expected to be 28*
            no_cols = int.from_bytes(f.read(4), byteorder="big")
            # Print out file details.
            # If parsed correctly, the values should be the same as the expected.
            print("File:",file,"\nMagic number: \t\t%10d\nNumber of Images: \t%10d\nNumber of Rows: \t%10d\nNumber of Columns: \t%10d\n" %(magic_num,no_images,no_rows,no_rows))

            pixel_list = [[[int.from_bytes(f.read(1), byteorder="big")for i in range(no_cols)] for j in range(no_rows)] for k in range(3)]

            print_image(pixel_list[2])

            return pixel_list
    finally:
        f.close()

def print_image(pixel_list):
    for i in pixel_list:
        for j in i:
            if( j < 127):
                print(".")
            else:
                print("#")

read_labels("data/train-labels-idx1-ubyte.gz")
read_images("data/train-images-idx3-ubyte.gz")
read_labels("data/t10k-labels-idx1-ubyte.gz")
read_images("data/t10k-images-idx3-ubyte.gz")