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


    