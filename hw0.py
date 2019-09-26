# This file, with a .py extension, contains a Python Program
# Lines that start with the hash sign are ignore by Python.
# they are used for comments. 
#
# To get started, we'll be using terminal to run our first
# Python programs this quarter. Terminal is an app that lets
# you type commands (at the command line or command prompt).
#
# This can be frustrating at first, as you need to remember
# or be able to look up what command to use. However, it 
# can be much more expressive and flexible than a graphical
# interface, because the vocabulary of possible commands is
# much greater than can be shown in a graphical interface.
#
# Step 1: To run this program, in a terminal window, type:
#
# cd ~/wherever your homework is stored 
#
# and then type "py -3.7 hw0.py" if you are using Windows
# or type "python3 hw0.py" if you are using MacOS
#
# If you aren't sure how to open a terminal window:
# On MacOS, you can hold ⌘ and hit the space bar.
# In the popup, type "terminal" and hit the enter key.
# On Windows, you can click the start button or hit the Windows key.
# Then, type "cmd" and hit the enter key.

def hello():
    print("--------------------------------")
    print("Welcome to HCDE 310.")
    print("")
    print("We are glad you are here")
    print("and we hope you enjoy the class.")
    print("--------------------------------")


hello()
print("... Let's say that again... \n")
hello()

# Step 2: Now try deleting the second hello(). Save the file.
# Run the program again to see the results.

# Step 3: Now insert "hello()" back into the editor buffer
# below this line. Try using the auto-complete feature. After
# you type "hel", possible completions should appear.
# Use the arrow keys or the mouse to select, and hit enter.

# Save the file. Run it again to see the results.

# Step 4: Now, try a Python program that uses variables. Uncomment
# the lines below, by removing the # at the start of each line. Fill
# in the values for length, width, height, and your name.
# Then save and run the program again.

length = 10
width = 34
height = 7

me = "Cecilia"
print("Volume =", width * length * height)
print("My name is", me)

# Step 5: You can also run Python programs in PyCharm as well.
# In PyCharm, click File and then New Project. Make sure the
# interpreter field contains Python 3, and navigate to the Homework
# folder. Click OK. In PyCharm, you should see the folder name
# displayed on the left. From there you can click and open hw0.py'.
#

# First, get a piece of paper and a pen. In order to count the number of words in a document, you must start from
# the top of the first page of the document and look for the first line of text. Once you find the first line of text,
# look at the word on the leftmost side of the line, and use the pen to make a small tally mark on the paper. Then,
# go to next word in the line, directly to the right of the word you just tallied, and use the pen and make another
# tally. Every word in the line gets one tally on the paper. Keep doing this, tallying once per word and moving to the
# right. Once you run out of words on the line, move down to the next line of text directly underneath the first line
# and repeat this process for the entirety of document, on every page. Once you have finished tallying for the whole
# document,Count the number of tally's on the page and total them. That total is the number of words on the document.
#
# I did find it challenging to try and give the instructions in English. It is hard to be exact and precise when
# words can easily be misinterpreted. I found myself constantly questioning if the person reading the directions
# would do the task properly. Numbers are much better! Also, I cant wait to learn a new language in this class
# and gain extra skills in data analysis. I want to do data science and enjoy coding so I think I will really enjoy
# my time in this class!
