#%%

def emissions ():
    yearOne = input("What is starting year of data collection?")
    emissionsOne = input("What is the value of emissions in {0}?".format(yearOne))
    yearTwo = input("What is the ending year of data collection?")
    emissionsTwo = input("What is the value of emissions in {0}".format(yearTwo))
    yearThree = input("For what year do you want to predict the emissions?")
    target = input("What is the target emissions value in {0}".format(yearThree))
    
    try:
        yearOne = int(yearOne)
        emissionsOne = float(emissionsOne)
        yearTwo = int(yearTwo)
        emissionsTwo = float(emissionsTwo)
        yearThree = int(yearThree)
    
    
    except:
        return ("Please only enter numerical values")
    
    slope = (emissionsTwo - emissionsOne)/(yearTwo - yearOne)
    intercept = emissionsOne - slope * yearOne
    emissionsThree = yearThree * slope + intercept
    output = "The emissions in {0} will be {1}".format(yearThree, emissionsThree)
    higher = emissionsThree > target
    if (higher == True):
        comparison = "\nThe target value for {0} will be exceeded.".format(yearThree)
    else:
        comparison = "\nThe target value for {0} will be exceeded.".format(yearThree)
    return (output, comparison)

print(emissions())
    
#%%

def emissions (yearOne, emissionsOne, yearTwo, emissionsTwo, yearThree, target):
    try:
        yearOne = int(yearOne)
        emissionsOne = float(emissionsOne)
        yearTwo = int(yearTwo)
        emissionsTwo = float(emissionsTwo)
        yearThree = int(yearThree)
        target = float(target)
    
    
    except:
        return ("Please only enter numerical values")
    
    slope = (emissionsTwo - emissionsOne)/(yearTwo - yearOne)
    intercept = emissionsOne - slope * yearOne
    emissionsThree = yearThree * slope + intercept
    output = "The emissions in {0} will be {1}".format(yearThree, emissionsThree)
    higher = emissionsThree > target
    if (higher == True):
        comparison = "\nThe target value for {0} will be exceeded.".format(yearThree)
    else:
        comparison = "\nThe target value for {0} will be exceeded.".format(yearThree)
    return (output, comparison)

def runner ():
    return emissions(1900, 30, 2000, 40, 2100, 40)

print(runner()[0], runner()[1])

#%%

def leapyear (year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return ("The year {0} is a leap year".format(year)) 
    else:
        return ("The year {0} is not a leap year".year(year))
    
print(leapyear(400))

#%%

def fibonacci(runs):
    fiboList = [1, 1]
    for i in range(runs):
        banana = fiboList[-1] + fiboList[-2]
        print(banana)
        fiboList.append(banana)
        
    return fiboList
            
printed = fibonacci(30)
print(printed)

#%%

def cube (number):
    number = int(number)
    return number**3

print(cube(3))

#%%

import matplotlib.pyplot as plt
fin = open('population_world.dat')
header = fin.readline()
unit = fin.readline()
list_year= []
list_pop= []
for line in fin:
    t1, p1 = line.strip().split('\t')
    list_year.append(int(t1))
    list_pop.append(int(p1))

plt.plot(list_year, list_pop)
plt.show()
plt.close()
        

    