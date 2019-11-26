#%% libraries
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

#%% data import
with open('population_countries.csv', 'r', encoding="utf-8", errors="ignore") as fin:
    datarray = listmaker(fin)

#%% Calculating Descriptive Stats

pop_arith_mean = np.mean(datarray)
pop_geo_mean = stats.gmean(datarray)
pop_median = np.median(datarray)
pop_mode = stats.mode(datarray)
pop_std = np.std(datarray)
pop_iqr = stats.iqr(datarray)
pop_skew = stats.skew(datarray)
pop_num_miss = sum(np.isnan(datarray))

#%% Plotting Other Stats

binlist = np.logspace(np.log(1000), np.log10(20000000000), 20)

plt.xkcd()
_ = plt.hist(datarray, bins=binlist)
_ = plt.xscale("log")
_ = plt.xlabel("Number of Inhabitants")
plt.show()

_ = plt.boxplot(datarray)
_ = plt.yscale("log")
_ = plt.ylabel("Number of Inhabitants")
plt.show()

#%%

def listmaker(file):
    population = []
    next(file)
    for line in fin:
        # enter your column separator below; are 3 variables representating 3 columns correct?
        c, p = line.strip().split(',')
        population.append(int(p))
    fin.close()
    return np.array(population)
    

# %%
