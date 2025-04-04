import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 设置字体为新罗马
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = '15'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

# 读取CSV文件

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

data2 = data.sort_values(by=u'cleanPower10000tonsofstand2006')
ele2 = data2[u'cleanPower10000tonsofstand2006'].values
population2 = data2[u'pop2006'].values

data22 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2006')
ele22 = data22[u'cleanPower10000tonsofstand2006'].values
population22 = data22[u'pop2006'].values

data222= data_Income1.sort_values(by=u'cleanPower10000tonsofstand2006')
ele222 = data222[u'cleanPower10000tonsofstand2006'].values
population222 = data222[u'pop2006'].values

data3 = data.sort_values(by=u'cleanPower10000tonsofstand2007')
ele3 = data3[u'cleanPower10000tonsofstand2007'].values
population3 = data3[u'pop2007'].values

data33 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2007')
ele33 = data33[u'cleanPower10000tonsofstand2007'].values
population33 = data33[u'pop2007'].values

data333 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2007')
ele333 = data333[u'cleanPower10000tonsofstand2007'].values
population333 = data333[u'pop2007'].values

data4 = data.sort_values(by=u'cleanPower10000tonsofstand2008')
ele4 = data4[u'cleanPower10000tonsofstand2008'].values
population4 = data4[u'pop2008'].values

data44 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2008')
ele44 = data44[u'cleanPower10000tonsofstand2008'].values
population44 = data44[u'pop2008'].values

data444 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2008')
ele444 = data444[u'cleanPower10000tonsofstand2008'].values
population444 = data444[u'pop2008'].values

data5 = data.sort_values(by=u'cleanPower10000tonsofstand2009')
ele5 = data5[u'cleanPower10000tonsofstand2009'].values
population5 = data5[u'pop2009'].values

data55 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2009')
ele55= data55[u'cleanPower10000tonsofstand2009'].values
population55 = data55[u'pop2009'].values

data555 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2009')
ele555 = data555[u'cleanPower10000tonsofstand2009'].values
population555 = data555[u'pop2009'].values

data6 = data.sort_values(by=u'cleanPower10000tonsofstand2010')
ele6= data6[u'cleanPower10000tonsofstand2010'].values
population6 = data6[u'pop2010'].values

data66 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2010')
ele66= data66[u'cleanPower10000tonsofstand2010'].values
population66 = data66[u'pop2010'].values

data666 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2010')
ele666 = data666[u'cleanPower10000tonsofstand2010'].values
population666 = data666[u'pop2010'].values

data7 = data.sort_values(by=u'cleanPower10000tonsofstand2011')
ele7= data7[u'cleanPower10000tonsofstand2011'].values
population7 = data7[u'pop2011'].values

data77 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2011')
ele77= data77[u'cleanPower10000tonsofstand2011'].values
population77 = data77[u'pop2011'].values

data777 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2011')
ele777 = data777[u'cleanPower10000tonsofstand2011'].values
population777 = data777[u'pop2011'].values

data8 = data.sort_values(by=u'cleanPower10000tonsofstand2012')
ele8= data8[u'cleanPower10000tonsofstand2012'].values
population8 = data8[u'pop2012'].values

data88 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2012')
ele88= data88[u'cleanPower10000tonsofstand2012'].values
population88 = data88[u'pop2012'].values

data888 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2012')
ele888 = data888[u'cleanPower10000tonsofstand2012'].values
population888 = data888[u'pop2012'].values

data9 = data.sort_values(by=u'cleanPower10000tonsofstand2013')
ele9= data9[u'cleanPower10000tonsofstand2013'].values
population9 = data9[u'pop2013'].values

data99 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2013')
ele99= data99[u'cleanPower10000tonsofstand2013'].values
population99 = data99[u'pop2013'].values

data999 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2013')
ele999 = data999[u'cleanPower10000tonsofstand2013'].values
population999 = data999[u'pop2013'].values

data2014 = data.sort_values(by=u'cleanPower10000tonsofstand2014')
ele2014= data2014[u'cleanPower10000tonsofstand2014'].values
population2014 = data2014[u'pop2014'].values

data10 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2014')
ele10= data10[u'cleanPower10000tonsofstand2014'].values
population10 = data10[u'pop2014'].values

data1010 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2014')
ele1010 = data1010[u'cleanPower10000tonsofstand2014'].values
population1010 = data1010[u'pop2014'].values

data2015 = data.sort_values(by=u'cleanPower10000tonsofstand2015')
ele2015= data2015[u'cleanPower10000tonsofstand2015'].values
population2015 = data2015[u'pop2015'].values

data1111 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2015')
ele1111= data1111[u'cleanPower10000tonsofstand2015'].values
population1111 = data1111[u'pop2015'].values

data111111 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2015')
ele111111 = data111111[u'cleanPower10000tonsofstand2015'].values
population111111 = data111111[u'pop2015'].values

data2016 = data.sort_values(by=u'cleanPower10000tonsofstand2016')
ele2016= data2016[u'cleanPower10000tonsofstand2016'].values
population2016 = data2016[u'pop2016'].values

data12 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2016')
ele12= data12[u'cleanPower10000tonsofstand2016'].values
population12 = data12[u'pop2016'].values

data1212 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2016')
ele1212 = data1212[u'cleanPower10000tonsofstand2016'].values
population1212 = data1212[u'pop2016'].values

data2017 = data.sort_values(by=u'cleanPower10000tonsofstand2017')
ele2017 = data2017[u'cleanPower10000tonsofstand2017'].values
population2017 = data2017[u'pop2017'].values

data13 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2017')
ele13 = data13[u'cleanPower10000tonsofstand2017'].values
population13 = data13[u'pop2017'].values

data1313 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2017')
ele1313 = data1313[u'cleanPower10000tonsofstand2017'].values
population1313 = data1313[u'pop2017'].values

data2018 = data.sort_values(by=u'cleanPower10000tonsofstand2018')
ele2018 = data2018[u'cleanPower10000tonsofstand2018'].values
population2018 = data2018[u'pop2018'].values

data14 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2018')
ele14 = data14[u'cleanPower10000tonsofstand2018'].values
population14 = data14[u'pop2018'].values

data1414 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2018')
ele1414 = data1414[u'cleanPower10000tonsofstand2018'].values
population1414 = data1414[u'pop2018'].values

data2019 = data.sort_values(by=u'cleanPower10000tonsofstand2019')
ele2019 = data2019[u'cleanPower10000tonsofstand2019'].values
population2019 = data2019[u'pop2019'].values

data15 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2019')
ele15 = data15[u'cleanPower10000tonsofstand2019'].values
population15 = data15[u'pop2019'].values

data1515= data_Income1.sort_values(by=u'cleanPower10000tonsofstand2019')
ele1515 = data1515[u'cleanPower10000tonsofstand2019'].values
population1515 = data1515[u'pop2019'].values

data2020 = data.sort_values(by=u'cleanPower10000tonsofstand2020')
ele2020 = data2020[u'cleanPower10000tonsofstand2020'].values
population2020 = data2020[u'pop2020'].values

data16 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2020')
ele16 = data16[u'cleanPower10000tonsofstand2020'].values
population16 = data16[u'pop2020'].values

data1616 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2020')
ele1616 = data1616[u'cleanPower10000tonsofstand2020'].values
population1616 = data1616[u'pop2020'].values

data2021 = data.sort_values(by=u'cleanPower10000tonsofstand2021')
ele2021 = data2021[u'cleanPower10000tonsofstand2021'].values
population2021 = data2021[u'pop2021'].values

data17 = data_Income.sort_values(by=u'cleanPower10000tonsofstand2021')
ele17 = data17[u'cleanPower10000tonsofstand2021'].values
population17 = data17[u'pop2021'].values

data1717 = data_Income1.sort_values(by=u'cleanPower10000tonsofstand2021')
ele1717 = data1717[u'cleanPower10000tonsofstand2021'].values
population1717 = data1717[u'pop2021'].values

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

cum_population4 = np.cumsum(population4) / np.sum(population4) * 100
cum_income4 = np.cumsum(ele4 * population4) / np.sum(ele4 * population4) * 100

cum_population44 = np.cumsum(population44) / np.sum(population44) * 100
cum_income44 = np.cumsum(ele44 * population44) / np.sum(ele44 * population44) * 100

cum_population444 = np.cumsum(population444) / np.sum(population444) * 100
cum_income444 = np.cumsum(ele444 * population444) / np.sum(ele444 * population444) * 100

cum_population5 = np.cumsum(population5) / np.sum(population5) * 100
cum_income5 = np.cumsum(ele5 * population5) / np.sum(ele5 * population5) * 100

cum_population55 = np.cumsum(population55) / np.sum(population55) * 100
cum_income55 = np.cumsum(ele55 * population55) / np.sum(ele55 * population55) * 100

cum_population555 = np.cumsum(population555) / np.sum(population555) * 100
cum_income555 = np.cumsum(ele555 * population555) / np.sum(ele555 * population555) * 100

cum_population6 = np.cumsum(population6) / np.sum(population6) * 100
cum_income6 = np.cumsum(ele6 * population6) / np.sum(ele6 * population6) * 100

cum_population66 = np.cumsum(population66) / np.sum(population66) * 100
cum_income66 = np.cumsum(ele66 * population66) / np.sum(ele66 * population66) * 100

cum_population666 = np.cumsum(population666) / np.sum(population666) * 100
cum_income666 = np.cumsum(ele666 * population666) / np.sum(ele666 * population666) * 100

cum_population7 = np.cumsum(population7) / np.sum(population7) * 100
cum_income7 = np.cumsum(ele7 * population7) / np.sum(ele7 * population7) * 100

cum_population77 = np.cumsum(population77) / np.sum(population77) * 100
cum_income77 = np.cumsum(ele77 * population77) / np.sum(ele77 * population77) * 100

cum_population777 = np.cumsum(population777) / np.sum(population777) * 100
cum_income777 = np.cumsum(ele777 * population777) / np.sum(ele777 * population777) * 100

cum_population8 = np.cumsum(population8) / np.sum(population8) * 100
cum_income8 = np.cumsum(ele8 * population8) / np.sum(ele8 * population8) * 100

cum_population88 = np.cumsum(population88) / np.sum(population88) * 100
cum_income88 = np.cumsum(ele88 * population88) / np.sum(ele88 * population88) * 100

cum_population888 = np.cumsum(population888) / np.sum(population888) * 100
cum_income888 = np.cumsum(ele888 * population888) / np.sum(ele888 * population888) * 100

cum_population9 = np.cumsum(population9) / np.sum(population9) * 100
cum_income9 = np.cumsum(ele9 * population9) / np.sum(ele9 * population9) * 100

cum_population99 = np.cumsum(population99) / np.sum(population99) * 100
cum_income99 = np.cumsum(ele99 * population99) / np.sum(ele99 * population99) * 100

cum_population999 = np.cumsum(population999) / np.sum(population999) * 100
cum_income999 = np.cumsum(ele999 * population999) / np.sum(ele999 * population999) * 100

cum_population2014 = np.cumsum(population2014) / np.sum(population2014) * 100
cum_income2014 = np.cumsum(ele2014 * population2014) / np.sum(ele2014 * population2014) * 100

cum_population10 = np.cumsum(population10) / np.sum(population10) * 100
cum_income10 = np.cumsum(ele10 * population10) / np.sum(ele10 * population10) * 100

cum_population1010 = np.cumsum(population1010) / np.sum(population1010) * 100
cum_income1010 = np.cumsum(ele1010 * population1010) / np.sum(ele1010 * population1010) * 100

cum_population2015 = np.cumsum(population2015) / np.sum(population2015) * 100
cum_income2015 = np.cumsum(ele2015 * population2015) / np.sum(ele2015 * population2015) * 100

cum_population1111 = np.cumsum(population1111) / np.sum(population1111) * 100
cum_income1111 = np.cumsum(ele1111 * population1111) / np.sum(ele1111 * population1111) * 100

cum_population111111 = np.cumsum(population111111) / np.sum(population111111) * 100
cum_income111111 = np.cumsum(ele111111 * population111111) / np.sum(ele111111 * population111111) * 100

cum_population2016 = np.cumsum(population2016) / np.sum(population2016) * 100
cum_income2016 = np.cumsum(ele2016 * population2016) / np.sum(ele2016 * population2016) * 100

cum_population12 = np.cumsum(population12) / np.sum(population12) * 100
cum_income12 = np.cumsum(ele12 * population12) / np.sum(ele12 * population12) * 100

cum_population1212 = np.cumsum(population1212) / np.sum(population1212) * 100
cum_income1212 = np.cumsum(ele1212 * population1212) / np.sum(ele1212 * population1212) * 100

cum_population2017 = np.cumsum(population2017) / np.sum(population2017) * 100
cum_income2017 = np.cumsum(ele2017 * population2017) / np.sum(ele2017 * population2017) * 100

cum_population13 = np.cumsum(population13) / np.sum(population13) * 100
cum_income13 = np.cumsum(ele13 * population13) / np.sum(ele13 * population13) * 100

cum_population1313 = np.cumsum(population1313) / np.sum(population1313) * 100
cum_income1313 = np.cumsum(ele1313 * population1313) / np.sum(ele1313 * population1313) * 100

cum_population2018 = np.cumsum(population2018) / np.sum(population2018) * 100
cum_income2018 = np.cumsum(ele2018 * population2018) / np.sum(ele2018 * population2018) * 100

cum_population14 = np.cumsum(population14) / np.sum(population14) * 100
cum_income14 = np.cumsum(ele14 * population14) / np.sum(ele14 * population14) * 100

cum_population1414 = np.cumsum(population1414) / np.sum(population1414) * 100
cum_income1414 = np.cumsum(ele1414 * population1414) / np.sum(ele1414 * population1414) * 100

cum_population2019 = np.cumsum(population2019) / np.sum(population2019) * 100
cum_income2019 = np.cumsum(ele2019 * population2019) / np.sum(ele2019 * population2019) * 100

cum_population15 = np.cumsum(population15) / np.sum(population15) * 100
cum_income15 = np.cumsum(ele15 * population15) / np.sum(ele15 * population15) * 100

cum_population1515 = np.cumsum(population1515) / np.sum(population1515) * 100
cum_income1515 = np.cumsum(ele1515 * population1515) / np.sum(ele1515 * population1515) * 100

cum_population2020 = np.cumsum(population2020) / np.sum(population2020) * 100
cum_income2020 = np.cumsum(ele2020 * population2020) / np.sum(ele2020 * population2020) * 100

cum_population16 = np.cumsum(population16) / np.sum(population16) * 100
cum_income16 = np.cumsum(ele16 * population16) / np.sum(ele16 * population16) * 100

cum_population1616 = np.cumsum(population1616) / np.sum(population1616) * 100
cum_income1616 = np.cumsum(ele1616 * population1616) / np.sum(ele1616 * population1616) * 100

cum_population2021 = np.cumsum(population2021) / np.sum(population2021) * 100
cum_income2021 = np.cumsum(ele2021 * population2021) / np.sum(ele2021 * population2021) * 100

cum_population17 = np.cumsum(population17) / np.sum(population17) * 100
cum_income17 = np.cumsum(ele17 * population17) / np.sum(ele17 * population17) * 100

cum_population1717 = np.cumsum(population1717) / np.sum(population1717) * 100
cum_income1717 = np.cumsum(ele1717 * population1717) / np.sum(ele1717 * population1717) * 100


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
gini1= "%.2f" % gini1

gini2 = gini_coefficient(ele2, population2)
gini2= "%.2f" % gini2

gini3 = gini_coefficient(ele3, population3)
gini3= "%.3f" % gini3

gini4 = gini_coefficient(ele4, population4)
print(f'2008清洁电力基尼系数: {gini4}')
gini4= "%.4f" % gini4

gini5 = gini_coefficient(ele5, population5)
print(f'2009清洁电力基尼系数: {gini5}')
gini5= "%.2f" % gini5

gini6 = gini_coefficient(ele6, population6)
gini6= "%.2f" % gini6

gini7 = gini_coefficient(ele7, population7)
gini7= "%.2f" % gini7

gini8 = gini_coefficient(ele8, population8)
gini8= "%.2f" % gini8

gini9 = gini_coefficient(ele9, population9)
gini9= "%.2f" % gini9

gini2014 = gini_coefficient(ele2014, population2014)
gini2014= "%.2f" % gini2014

gini2015 = gini_coefficient(ele2015, population2015)
gini2015= "%.2f" % gini2015

gini2016 = gini_coefficient(ele2016, population2016)
gini2016= "%.2f" % gini2016

gini2017 = gini_coefficient(ele2017, population2017)
gini2017= "%.2f" % gini2017

gini2018 = gini_coefficient(ele2018, population2018)
gini2018= "%.2f" % gini2018

gini2019 = gini_coefficient(ele2019, population2019)
gini2019= "%.2f" % gini2019

gini2020 = gini_coefficient(ele2020, population2020)
gini2020= "%.2f" % gini2020

gini2021 = gini_coefficient(ele2021, population2021)
gini2021= "%.2f" % gini2021

gini11 = gini_coefficient(ele11, population11)
gini11= "%.2f" % gini11

gini111 = gini_coefficient(ele111, population111)
gini111 = "%.2f" % gini111

gini22 = gini_coefficient(ele22, population22)
gini22 = "%.2f" % gini22

gini222 = gini_coefficient(ele222, population222)
gini222 = "%.2f" % gini222

gini33 = gini_coefficient(ele33, population33)
gini33 = "%.2f" % gini33

gini333 = gini_coefficient(ele333, population333)
gini333 = "%.2f" % gini333

gini44 = gini_coefficient(ele44, population44)
gini44 = "%.2f" % gini44

gini444 = gini_coefficient(ele444, population444)
gini444 = "%.2f" % gini444

gini55 = gini_coefficient(ele55, population55)
gini55 = "%.2f" % gini55

gini555 = gini_coefficient(ele555, population555)
gini555 = "%.2f" % gini555

gini66 = gini_coefficient(ele66, population66)
gini66 = "%.2f" % gini66

gini666 = gini_coefficient(ele666, population666)
gini666 = "%.2f" % gini666

gini77 = gini_coefficient(ele77, population77)
gini77 = "%.2f" % gini77

gini777 = gini_coefficient(ele777, population777)
gini777 = "%.2f" % gini777

gini88 = gini_coefficient(ele88, population88)
gini88 = "%.2f" % gini88

gini888 = gini_coefficient(ele888, population888)
gini888 = "%.2f" % gini888

gini99 = gini_coefficient(ele99, population99)
gini99 = "%.2f" % gini99

gini999 = gini_coefficient(ele999, population999)
gini999 = "%.2f" % gini999


gini10 = gini_coefficient(ele10, population10)

gini1010 = gini_coefficient(ele1010, population1010)


gini11 = gini_coefficient(ele11, population11)

gini1111 = gini_coefficient(ele1111, population1111)

gini12 = gini_coefficient(ele12, population12)

gini1212 = gini_coefficient(ele1212, population1212)

gini13 = gini_coefficient(ele13, population13)

gini1313 = gini_coefficient(ele1313, population1313)

gini14 = gini_coefficient(ele14, population14)

gini1414 = gini_coefficient(ele1414, population1414)

gini15 = gini_coefficient(ele15, population15)

gini1515 = gini_coefficient(ele1515, population1515)

gini16 = gini_coefficient(ele16, population16)

gini1616 = gini_coefficient(ele1616, population1616)

gini17 = gini_coefficient(ele17, population17)

gini1717 = gini_coefficient(ele1717, population1717)
