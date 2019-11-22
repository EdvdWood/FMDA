#%% Chapter 6: Exercise 1

def reverser (string):
    index = -1
    while -index <= len(string):
        print(string[index])
        index -= 1
        
reverser("Banana")
reverser("Florine")
reverser("Eddie")

#%% Exercise 2

fruit = "Banana"
print(fruit[:])

# It means to print all parts of the string

#%% Exercise 3

def count (word, target):
    count = 0
    for letter in word:
        if letter == target:
            count = count + 1
    print(count)

count("Banana", "a")

#%% Exercise 4

print("banana".count("a"))

#%% Exercise 5
given = "X-DSPAM-Confidence:0.8475"

def returner(given):
    return float(given[given.find(":")+1:])

print(returner(given))

#%% Chapter 7: Exercise 1

def reader(File_Name):
    file = open(File_Name, "r")
    for line in file:
        print(line.upper())
        
reader("workshop2.txt")

#%% Exercise 2

import numpy as np

def reader(File_Name):
    file = open(File_Name, "r")
    conflog = list()
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
           confidence = float(line[line.find(":")+1:]) 
           conflog.append(confidence)
    return("File: {0} \nAverage spam confidence: {1}".format(File_Name,np.mean(conflog)))  
        
        
print(reader("workshop2.txt"))

#%% Exercise 3

import numpy as np

def reader(File_Name):
    if File_Name == "na na boo boo": return ("File: na na boo boo\nNA NA BOO BOO TO YOU - You have been punk'd!")
    file = open(File_Name, "r")
    conflog = list()
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
           confidence = float(line[line.find(":")+1:]) 
           conflog.append(confidence)
    return("File: {0} \nAverage spam confidence: {1}".format(File_Name,np.mean(conflog)))  
        
        
print(reader("workshop2.txt"))
print(reader("na na boo boo"))

#%% Chapter 8 Exercise 1

def chop (inList):
    inList = inList[1:-1]
    return None
    
def middle (inList):
    return inList[1:-1]

chop([1,2,3])
middle([1,2,3])

#%% Exercise 2

fhand = open('workshop2.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    try:
        print(words[2])
    except:
        continue
    
# It can still go wrong if a line has length 1 and starts with "From: "
    
#%% Exercise 3

fhand = open('workshop2.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' : continue
    try:
        print(words[2])
    except:
        continue
    
#%% Exercise 4



def dicfunc (filename):
    dictionary = []
    fhand = open(filename, "r")
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in dictionary:
                dictionary.append(word)
    dictionary.sort()
    return dictionary

print(dicfunc("workshop2_file2.txt"))

#%% Exercise 5

def fromcount (filename):
    fhand = open(filename, "r")
    counter = 0
    for line in fhand:
        if line.startswith("From"):
            counter += 1
            text = line.split()
            print (text[1])
        else:
            continue
    print("There were {0} lines in the file with From as the first word.".format(counter))

fromcount("workshop2.txt")

#%% Exercise 6

def numbercounter ():
    numberlist = []
    while True:
        value = input("Please enter numeric values or enter 'done' to exit")
        if value == "done":
            break
        try:
            value = float(value)
        except:
            print("Numeric values only please")
            continue
        numberlist.append(value)
    return("Max: {0}\nMin:{1}".format(max(numberlist), min(numberlist)))

print(numbercounter())