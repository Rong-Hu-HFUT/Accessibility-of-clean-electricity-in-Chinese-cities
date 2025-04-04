import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = '18'
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


data = pd.read_excel(r"Ele-Pub.xlsx")
data_Income = pd.read_excel(r"博台线-西 Ele-Pub.xlsx")
data_Income1 = pd.read_excel(r"博台线-东 Ele-Pub.xlsx")

data1 = data.sort_values(by=u'cleanPower10000tonsofstand2005')
ele1 = data1[u'cleanPower10000tonsofstand2005'].values
population1 = data1[u'pop2005'].values

data11 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2005')
ele11 = data11[u'cleanPower10000tonsofstand2005'].values
population11 = data11[u'pop2005'].values

data111 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2005')
ele111 = data111[u'cleanPower10000tonsofstand2005'].values
population111 = data111[u'pop2005'].values

data2 = data.sort_values(by=u'cleanPower10000tonsofstand2015')
ele2 = data2[u'cleanPower10000tonsofstand2015'].values
population2 = data2[u'pop2015'].values

data22 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2015')
ele22 = data22[u'cleanPower10000tonsofstand2015'].values
population22 = data22[u'pop2015'].values

data222= data_Income1.sort_values(by=u'cleanPower10000tonsofstand2015')
ele222 = data222[u'cleanPower10000tonsofstand2015'].values
population222 = data222[u'pop2015'].values

data3 = data.sort_values(by=u'cleanPower10000tonsofstand2021')
ele3 = data3[u'cleanPower10000tonsofstand2021'].values
population3 = data3[u'pop2021'].values

data33 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2021')
ele33 = data33[u'cleanPower10000tonsofstand2021'].values
population33 = data33[u'pop2021'].values

data333 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2021')
ele333 = data333[u'cleanPower10000tonsofstand2021'].values
population333 = data333[u'pop2021'].values



cum_population1 = np.cumsum(population1) / np.sum(population1) * 100
cum_income1 = np.cumsum(ele1 * population1) / np.sum(ele1 * population1) * 100

cum_population11 = np.cumsum(population11) / np.sum(population11) * 100
cum_income11 = np.cumsum(ele11 * population11) / np.sum(ele11 * population11) * 100

cum_population111 = np.cumsum(population111) / np.sum(population111) * 100
cum_income111 = np.cumsum(ele111 * population111) / np.sum(ele111 * population111) * 100

cum_population2 = np.cumsum(population2) / np.sum(population2) * 100
cum_income2 = np.cumsum(ele2 * population2) / np.sum(ele2 * population2) * 100

cum_population22 = np.cumsum(population22) / np.sum(population22) * 100
cum_income22 = np.cumsum(ele22 * population22) / np.sum(ele22 * population22) * 100

cum_population222 = np.cumsum(population222) / np.sum(population222) * 100
cum_income222 = np.cumsum(ele222 * population222) / np.sum(ele222 * population222) * 100

cum_population3 = np.cumsum(population3) / np.sum(population3) * 100
cum_income3 = np.cumsum(ele3 * population3) / np.sum(ele3 * population3) * 100

cum_population33 = np.cumsum(population33) / np.sum(population33) * 100
cum_income33 = np.cumsum(ele33 * population33) / np.sum(ele33 * population33) * 100

cum_population333 = np.cumsum(population333) / np.sum(population333) * 100
cum_income333 = np.cumsum(ele333 * population333) / np.sum(ele333 * population333) * 100

def gini_coefficient(income, population):
    n = len(income)
    index = np.arange(1, n + 1)
    income_population_product = income * population
    cumulative_income = np.cumsum(income_population_product)
    relative_income = cumulative_income / np.sum(income_population_product)
    relative_population = np.cumsum(population) / np.sum(population)
    B = np.trapz(relative_income, relative_population)
    A = 0.5 - B
    return A / (A + B)

gini1 = gini_coefficient(ele1, population1)

gini1 = "%.4f" % gini1

gini11 = gini_coefficient(ele11, population11)

gini11= "%.4f" % gini11

gini111 = gini_coefficient(ele111, population111)

gini111 = "%.4f" % gini111

gini2 = gini_coefficient(ele2, population2)

gini2 = "%.4f" % gini2

gini22 = gini_coefficient(ele22, population22)

gini22 = "%.4f" % gini22

gini222 = gini_coefficient(ele222, population222)

gini222 = "%.4f" % gini222

gini3 = gini_coefficient(ele3, population3)

gini3 = "%.4f" % gini3

gini33 = gini_coefficient(ele33, population33)

gini33 = "%.4f" % gini33

gini333 = gini_coefficient(ele333, population333)

gini333 = "%.4f" % gini333

custom_palette = sns.color_palette(["#99ADFF", "#C77CFF", "#F89999", "#C7A3B5", "#9B9CBD", "#788AB6", "#5B679B", "#5a6cca", "#A0BADB",
                                    "#9999C9"])
plt.rcParams['lines.linewidth'] = 2

sns.set_palette(custom_palette)

plt.figure(dpi=300,figsize=(8, 6))
plt.plot(cum_population1, cum_income1, linestyle='--', label=f'2005 Clean electricity consumption({gini1})')
plt.plot(cum_population11, cum_income11, linestyle='--', label=f'2005 Western clean electricity consumption ({gini11})')
plt.plot(cum_population111, cum_income111, linestyle='--', label=f'2005 Eastern clean electricity consumption ({gini111})')
plt.fill_between(cum_population1, cum_income1, cum_population1, color='#D9DEE7', alpha=0.5)
plt.plot(cum_population1, cum_population1, linestyle='--', color='black',)

plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xlabel('Cumulative population (%)')
plt.ylabel('Cumulative inequality indications (%)')


plt.legend(bbox_to_anchor=(0.925, 1),loc=4, frameon=False)
plt.tight_layout()
plt.savefig(r"2005 城市-清洁电力平等度量.png",)


plt.figure(dpi=300,figsize=(8, 6))
plt.plot(cum_population2, cum_income2, linestyle='--', label=f'2015 Clean electricity ({gini2})') #color='b',
plt.plot(cum_population22, cum_income22, linestyle='--', label=f'2015 Western clean electricity consumption ({gini22})') #color='b',
plt.plot(cum_population222, cum_income222, linestyle='--', label=f'2015 Eastern clean electricity consumption ({gini222})') #color='b',
plt.fill_between(cum_population2, cum_income2, cum_population2, color='#D9DEE7', alpha=0.5)
plt.plot(cum_population2, cum_population2,linestyle='--', color='black',)


plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xlabel('Cumulative population (%)')
plt.ylabel('Cumulative inequality indications (%)')

# 添加图例
plt.legend(bbox_to_anchor=(0.925, 1),loc=4, frameon=False)
plt.tight_layout()
plt.savefig(r"2015 城市-清洁电力平等度量.png",)

plt.figure(dpi=300,figsize=(8, 6))
plt.plot(cum_population3, cum_income3, linestyle='--', label=f'2021 Clean electricity ({gini3})')
plt.plot(cum_population33, cum_income33, linestyle='--', label=f'2021 Western clean electricity consumption ({gini33})')
plt.plot(cum_population333, cum_income333, linestyle='--', label=f'2021 Eastern clean electricity consumption ({gini333})')
plt.fill_between(cum_population3, cum_income3, cum_population3, color='#D9DEE7', alpha=0.5)
plt.plot(cum_population3, cum_population3, linestyle='--', color='black',)


plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xlabel('Cumulative population (%)')
plt.ylabel('Cumulative inequality indications (%)')


plt.legend(bbox_to_anchor=(0.925, 1),loc=4, frameon=False)
plt.tight_layout()
plt.savefig(r"2021 城市-清洁电力平等度量.png",)


plt.show()