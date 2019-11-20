#%% exercise 1

5
x = 5
x + 1

#%%

name = input("Enter your name!")
print("Hello", name)

#%%

hours = int(input("How many hours have you worked?"))
rate = float(input("How much do you earn?"))
pay = hours*rate
print("You have earned", pay)

#%%
width = 17
height = 12.0

Ex1 = width//2
Ex2 = width/2.0
Ex3 = height/3
Ex4 = 1 + 2 * 5

#%%

def fahrenheit ():
    tempC = input("What is the Celsius temperature?")
    tempF = tempC * 9/5 + 32
    print("In Fahrenheit, that is: ", tempF)

fahrenheit