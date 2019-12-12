#%%
import numpy as np
import scipy.stats as stats

obs = np.array ([1,3,5,4,6,7,9,8,10,12])
sim = np.arange(1,11)

print(len(obs), len(sim))

#%%

def summarizer(obs, sim):
    print ("Pbias:", pbiasser(obs, sim))
    print ("MAE:", maer(obs, sim))
    print ("RSME:", rooter(obs, sim))
    print ("NRSME:", normrooter(obs, sim))
    print ("r:", stats.pearsonr(obs, sim)[0])
    print ("R^2", stats.pearsonr(obs, sim)[0]**2)
    
    
    
#%%

def pbiasser(obs, sim):
    midval = []
    for i in range(len(obs)):
        midval.append(sim[i]-obs[i])
    pbias = 100 * (sum(midval)/sum(obs))
    return pbias
    
def maer(obs, sim):
    midval = []
    for i in range(len(obs)):
        midval.append(abs(sim[i]-obs[i]))
    mae = sum(midval)/len(midval)
    return mae
    
def rooter(obs, sim):
    midval = []
    for i in range(len(obs)):
        midval.append((sim[i]-obs[i])**2)
    root = np.sqrt(sum(midval)/len(midval))
    return root
    
def normrooter(obs, sim): 
    root = rooter(obs, sim)
    normroot = root / np.std(obs)
    return normroot




# %%

summarizer(obs, sim)

# %%
