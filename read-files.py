# Read files written by Ervin Mamutov, github/imervin

# Adapated code from
#       https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#       

import gzip

f = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')
initialByte = f.read(1)
print (int.from_bytes(initialByte, byteorder="big"))

f.close()