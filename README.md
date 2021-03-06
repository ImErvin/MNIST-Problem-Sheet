## MNIST Problem Sheet
This is a simple MNIST problem sheet. The aim of this problem sheet is to get a foot in the door and start learning about deep learning. This problem sheet was created by [Ian Mcloughlin](https://github.com/ianmcloughlin) as part of our emerging technologies module in college.

You can find my solutions to each of these problems in this repository.

### How to use this repository

1. Ensure you have Python 3.x and Git installed locally.
2. Enter the following commands into your command line.
```bash
# Change directory to anywhere you desire
cd anywhere..

# Clone this repository using git
git clone https://github.com/ImErvin/MNIST-Problem-Sheet.git
cd MNIST-Problem-Sheet

# Run the setup.py file
py setup.py

# Once setup.py has finished downloading, run the MNIST.py file
py MNIST.py

```

### What is MNIST?
MNIST(Modified National Institute of Standards and Technology) is a sub data set of NIST(National Institute of Standards and Technology), a large database of handwritten digits. MNIST is used to train image processing systems and is basically the "hello world" of computer vision.

MNIST contains 60,000 training images and 10,000 testing images. Training images are used to train a system, and testing images are used to test the trained system.

### Where does the MNIST dataset come from?
The set of images in the MNIST database is a combination of two of NIST's databases: Special Database 1 and Special Database 3. Special Database 1 and Special Database 3 consist of digits written by high school students and employees of the United States Census Bureau, respectively.[1]

### Sample images from the MNIST data set
Hold your mouse over the image to reveal the image label.
#### Training
![alt text](https://github.com/ImErvin/MNIST-Problem-Sheet/blob/master/images/train-00001-5.png?raw=true "Figure 5")
![alt text](https://github.com/ImErvin/MNIST-Problem-Sheet/blob/master/images/train-00002-0.png?raw=true "Figure 0")
![alt text](https://github.com/ImErvin/MNIST-Problem-Sheet/blob/master/images/train-00003-4.png?raw=true "Figure 4")

#### Testing
![alt text](https://github.com/ImErvin/MNIST-Problem-Sheet/blob/master/images/test-00001-7.png?raw=true "Figure 7")
![alt text](https://github.com/ImErvin/MNIST-Problem-Sheet/blob/master/images/test-00002-2.png?raw=true "Figure 2")
![alt text](https://github.com/ImErvin/MNIST-Problem-Sheet/blob/master/images/test-00003-1.png?raw=true "Figure 1")

### Problem Sheet Questions

**1. Read the data files**

	Download the image and label files. 
    Have Python decompress and read them byte by byte into appropriate data structures in memory.
**2. Output an image to the console**
	
	Output the third image in the training set to the console. 
    Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.
**3. Output the image files as PNGs**
	
	Use Python to output the image files as PNGs, saving them in a subfolder in your repository. 
    Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number 
    (where it occurs in the data file) and Y is its label. 
    For instance, the five-thousandth training image is labelled 2, so its file name should be train-05000-2.png.
    Commit these image files to GitHub.

### References
[1] [Wikipedia](https://en.wikipedia.org/wiki/MNIST_database)
