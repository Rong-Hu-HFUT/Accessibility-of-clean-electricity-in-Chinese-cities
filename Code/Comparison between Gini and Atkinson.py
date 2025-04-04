import pandas as pd
import numpy as np

# 读取数据
data = pd.read_excel(r"F:\数据和代码下载\不平等 数据\wide 清洁电力-人口.xlsx")

# 提取电力消费和人口数据
data1 = data.sort_values(by=u'cleanPower10000tonsofstand2005')
ele1 = data1[u'cleanPower10000tonsofstand2005'].values
population1 = data1[u'pop2005'].values

data2 = data.sort_values(by=u'cleanPower10000tonsofstand2015')
ele2 = data2[u'cleanPower10000tonsofstand2015'].values
population2 = data2[u'pop2015'].values

data3 = data.sort_values(by=u'cleanPower10000tonsofstand2021')
ele3 = data3[u'cleanPower10000tonsofstand2021'].values
population3 = data3[u'pop2021'].values

# 确保数据有效
def check_validity(ele):
    if np.any(ele < 0):
        raise ValueError("Error")
    return True

check_validity(ele1)

def atkinson_index(income, epsilon=0.5):  # 将epsilon默认值设置为0.5
    mean_income = np.mean(income)
    print(f'mean_income: {mean_income}')  # 调试输出
    if mean_income <= 0:
        return np.nan
    return 1 - (np.mean((income / mean_income) ** (1 - epsilon))) ** (1 / (1 - epsilon))


atkinson1 = atkinson_index(ele1)  # 确保epsilon的默认值是0.5
print(f'2005清洁电力Atkinson系数: {atkinson1}')


atkinson2 = atkinson_index(ele2)  # 确保epsilon的默认值是0.5
print(f'2015清洁电力Atkinson系数: {atkinson2}')



atkinson3 = atkinson_index(ele3)  # 确保epsilon的默认值是0.5
print(f'2021清洁电力Atkinson系数: {atkinson3}')

# 数据保存到Excel
results = {
    'Year': ['2005', '2015', '2021'],
    'Atkinson Coefficient': [atkinson1,atkinson2,atkinson3]
}
results_df = pd.DataFrame(results)
