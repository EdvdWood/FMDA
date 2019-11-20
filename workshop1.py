#%% Exercise 3.1

hours = float(input("Please input your hours"))
rate = float(input("Please input your hourly rate"))
if hours > 40:
    pay = 40*rate + (hours-40)*rate*1.5
else:
    pay = rate*hours
print(pay)
        

#%% Exercise 3.2

hours = float(input("Please input your hours"))
rate = float(input("Please input your hourly rate"))
try:
    if hours > 40:
        pay = 40*rate + (hours-40)*rate*1.5
    else:
        pay = rate*hours
    print(pay)      
except:
    print("Error, please enter numeric input")

#%% Exercise 3.3

def grader (score):
    try:
        if (score < 1.0 and score > 0.0):
            if score >= 0.9:
                grade = "A"
            elif score >= 0.8:
                grade = "B"
            elif score >= 0.7:
                grade = "C"
            elif score >= 0.6:
                grade = "D"
            elif score < 0.6:
                grade = "F"
            return grade
        else:
            return "Bad Score"
    except:
        return "Bad Score"

print(grader("Banana"))
print(grader(0.33))
print(grader(0.78))
print(grader(10.0))


#%% Exercise 4.1

import random

for i in range (10):
    x = random.random()
    print(x)

#%% Exercise 4.2 & 4.3


def repeat_lyrics():
    printlyrics()
    printlyrics()
    
def printlyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()

# 4.2: NameError
# 4.3: It runs.

#%% Exercise 4.4 & 4.5

# 4.4: D
# 4.5: D

#%% Exercise 4.6

def computePay (hours, rate):
    try:
        if hours > 40:
            pay = 40*rate + (hours-40)*rate*1.5
        else:
            pay = rate*hours
        print(pay)      
    except:
        print("Error, please enter numeric input")

computePay("Banana", 40)
computePay(33, 20)

#%% Exercise 4.7

def computerGrader (score):
    try:
        if (score < 1.0 and score > 0.0):
            if score >= 0.9:
                grade = "A"
            elif score >= 0.8:
                grade = "B"
            elif score >= 0.7:
                grade = "C"
            elif score >= 0.6:
                grade = "D"
            elif score < 0.6:
                grade = "F"
            return grade
        else:
            return "Bad Score"
    except:
        return "Bad Score"

print(computerGrader("Banana"))
print(computerGrader(0.33))
print(computerGrader(0.78))
print(computerGrader(10.0))

#%% Exercise 5.1 I made it work

def counter():
    inplist = []
    while True:
        line = input("Please enter a number or 'done'")
        if line == "done":
            break
        else:
            try:
                line = float(line)
                inplist.append(line)
            except:
                print("Invalid input")
    print(inplist)
    if len(inplist) > 0:
        print(sum(inplist)/len(inplist))
    else:
        print("No values were given")

counter()

#%% 5.2
        
        
def counter():
    inplist = []
    while True:
        line = input("Please enter a number or 'done'")
        if line == "done":
            break
        else:
            try:
                line = float(line)
                inplist.append(line)
            except:
                print("Invalid input")
    print(inplist)
    if len(inplist) > 0:
        print("The lowest value was:", min(inplist))
        print("The highest value was:", max(inplist))
    else:
        print("No values were given")

counter()
    
        
        
        
