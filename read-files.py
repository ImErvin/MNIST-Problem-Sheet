# Read files written by Ervin Mamutov, github/imervin

# Adapated code from
#       Unzip gz files        
#        - https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#       Read bytes from files 
#         - https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar
#       Read bytes from files 
#         - https://stackoverflow.com/questions/1035340/reading-binary-file-and-looping-over-each-byte
#       Create 3D array       
#         - https://stackoverflow.com/questions/10668341/create-3d-array-using-python
#       Saving as PNG image   
#         - https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image
#       Saving as PNG image
#         - https://stackoverflow.com/questions/4711880/pil-using-fromarray-with-binary-data-and-writing-coloured-text
#       Padding 0s to image file name
#         - https://stackoverflow.com/questions/339007/nicest-way-to-pad-zeroes-to-string

# Importing gzip to unzip a gz compressed files.
import gzip
# Importing numpy to convert lists into arrays.
import numpy as numpy
# Importing PIL to convert arrays into images.
from PIL import Image

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
# read_labels will read the label files and return a list of labels.
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
            
            # Create a list of labels -
            # I don't have the processing power to loop over each label/image so I just use the first
            # n images where n = no_labels / 1000. I can assume if it works for n images, it will work for
            # all of the images.
            # Looping over the number of labels divided 1000 and reading in each label 1 by 1.
            label_list = [int.from_bytes(f.read(1), byteorder="big") for i in range(int(no_labels / 1000))]

            # Return the list of labels to be used in different functions.
            return label_list
    finally:
        # Close the file after using it.
        f.close()

# read_images will read the image files and return a list of pixels for each image.
def read_images(file):
    try:
        with gzip.open(file) as f:
            # Magic number - *Expected to be 2051*
            magic_num = int.from_bytes(f.read(4), byteorder="big")

            # Number of images - *Expected to be 60000 training files & 10000 testing files*
            no_images = int.from_bytes(f.read(4), byteorder="big")

            # Number of rows - *Expected to be 28*
            no_rows = int.from_bytes(f.read(4), byteorder="big")

            # Number of columns - *Expected to be 28*
            no_cols = int.from_bytes(f.read(4), byteorder="big")

            # Print out file details.
            # If parsed correctly, the values should be the same as the expected.
            print("File:",file,"\nMagic number: \t\t%10d\nNumber of Images: \t%10d\nNumber of Rows: \t%10d\nNumber of Columns: \t%10d\n" %(magic_num,no_images,no_rows,no_rows))

            # Create a 3D list of image pixels - 
            # I don't have the processing power to loop over each label/image so I just use the first
            # n images where n = no_labels / 1000. I can assume if it works for n images, it will work for
            # all of the images.
            # Using Pythons use of nested angle brackets and logic within the angle brackets.
            # 1. The first angle brackets will loop over the number of images divided by 1000
            # 2. The second angle brackets will loop over the amount of rows.
            # 3. The third and final angle brackets will loop over the amount of columns and record the pixel value (0-255).
            pixel_list = [[[int.from_bytes(f.read(1), byteorder="big")for i in range(no_cols)] for j in range(no_rows)] for k in range(int(no_images / 1000))]

            # Return the list of pixels to be used in different functions.
            return pixel_list
    finally:
        # Close the file after using it.
        f.close()

# print_image will recieve a list of pixels and print out a visual representation of the image to the console.
def print_image(pixel_list):
    # Loop over the number of rows in the pixel list.
    for i in pixel_list:
        # Prints out a new line after each row.
        print("\n")
        # Loop over the number of columns in the rows
        for j in i:
            # If the column value is less than 128, print out "." - This represents a white pixel.
            if( j < 128):
                print(".", end="")
            # Or else if the column is greater than 128, print out "#" - This represents a black pixel.
            else:
                print("#", end="")

# save_image will recieve a list of pixels, an integer index, an integer label and a boolean train_test.
# These parameters will be used to create the image and the image's file name.
# Problem sheet states to use the following format:
# "train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label."
# The pixel list is used to read in each value and transfer it into an image using PIL's Image tool.
# The index is used to indentify where the image number occurs in the datafile (training_images).
# The label is used to identify the number that is shown in the picture.
# The train_test is a boolean to determine if the image's are part of the train images or test images.
def save_image(pixel_list, index, label, train_test):
    # Instantiate an empty string.
    file_format = ""

    # If the train_test value is true, change the empty string to "train-xxxxx-y" format.
    if(train_test):
        # Using the string format %05d and %d to add variables to the string.
        # %05d adds 0s to the left if not enough integers.
        file_format = "images/train-%05d-%d.png"
    # If the train_test value is false, change the empty string to "test-xxxxx-y" format.
    else:
        # Using the string format %05d and %d to add variables to the string.
        # %05d adds 0s to the left if not enough integers.
        file_format = "images/test-%05d-%d.png"
    
    # Using numpys .array() function to turn the list into a numpy array.
    pixel_array = numpy.array(pixel_list)

    # Turn the array into an image, using Pillow's Image.fromarray() 
    # to an image memory from an object exporting the array interface and converting to
    # "RGB" to save file locally.
    image = Image.fromarray(pixel_array).convert("RGB")

    # Saving the file and inserting the correct variables into the string for the "train/test-xxxxx-y" format.
    image.save(file_format %(index,label))

# List of labels for the training images.
training_labels = read_labels("data/train-labels-idx1-ubyte.gz")
# List of pixels representing the training images.
training_images = read_images("data/train-images-idx3-ubyte.gz")
# List of labels for the testing images.
testing_labels = read_labels("data/t10k-labels-idx1-ubyte.gz")
# List of pixels representing the testing images.
testing_images = read_images("data/t10k-images-idx3-ubyte.gz")

# Call the print_image function to print out the 3rd image to the screen
print_image(training_images[2])

# Loop that starts at 1, the length of training/testing_images+1 and increments by 1.
# Each iteration will save the image at the current index i - 1 (as the loop starts at 1 and ends at 60).
for i in range(1,len(training_images)+1,1):
    save_image(training_images[i-1], i, training_labels[i-1], True)

for i in range(1,len(testing_images)+1,1):
    save_image(testing_images[i-1], i, testing_labels[i-1], False)