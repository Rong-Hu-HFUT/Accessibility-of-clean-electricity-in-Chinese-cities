import pandas as pd
import numpy as np


data1 = data.sort_values(by=u'cleanPower10000tonsofstand2005')
ele1 = data1[u'cleanPower10000tonsofstand2005'].values
population1 = data1[u'pop2005'].values

data2 = data.sort_values(by=u'cleanPower10000tonsofstand2015')
ele2 = data2[u'cleanPower10000tonsofstand2015'].values
population2 = data2[u'pop2015'].values

data3 = data.sort_values(by=u'cleanPower10000tonsofstand2021')
ele3 = data3[u'cleanPower10000tonsofstand2021'].values
population3 = data3[u'pop2021'].values

def check_validity(ele):
    if np.any(ele < 0):
        raise ValueError("Error")
    return True

check_validity(ele1)

def atkinson_index(income, epsilon=0.5): 
    mean_income = np.mean(income)
    print(f'mean_income: {mean_income}') 
    if mean_income <= 0:
        return np.nan
    return 1 - (np.mean((income / mean_income) ** (1 - epsilon))) ** (1 / (1 - epsilon))


atkinson1 = atkinson_index(ele1)  
print(f'2005 Atkinson: {atkinson1}')


atkinson2 = atkinson_index(ele2) 
print(f'2015 Atkinson: {atkinson2}')



atkinson3 = atkinson_index(ele3) 
print(f'2021 Atkinson: {atkinson3}')

results = {
    'Year': ['2005', '2015', '2021'],
    'Atkinson Coefficient': [atkinson1,atkinson2,atkinson3]
}
results_df = pd.DataFrame(results)
