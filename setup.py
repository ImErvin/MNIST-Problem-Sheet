# Setup written by Ervin Mamutov, github/imervin

# Adapated code from
#       Download file from URL       
#        -  https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
#       Use Operating System commands 
#         - https://stackoverflow.com/questions/1274405/how-to-create-new-folder

# Import OS to use operating system commands
import os
# Import urllib.request to make a HTTP request.
import urllib.request

# Create a directory "data"
os.makedirs("./data")
# Change directory to "data"
os.chdir("./data")

print("Downloading Files... (This may take a while depending on your internet connection)")

# Use urllib's request to retrieve the gzip files from yann.lecun.com and save them into the current directory.
urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz', 'train-images-idx3-ubyte.gz')
urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz', 'train-labels-idx1-ubyte.gz')
urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz', 't10k-images-idx3-ubyte.gz')
urllib.request.urlretrieve('http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz', 't10k-labels-idx1-ubyte.gz')

print("Download Complete! You can now run > py MNIST.py")