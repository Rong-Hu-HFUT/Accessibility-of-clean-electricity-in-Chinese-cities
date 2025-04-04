import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.utils import resample

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = '15'
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
 
data = pd.read_excel(r"random forest regression.xlsx")

X = data.drop(columns=['lnCleanpowertonsofstandardcoal'])
y = data['lnCleanpowertonsofstandardcoal']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

results = X_test.copy()
results['Actual_Cleanpower'] = y_test.values
results['Predicted_Cleanpower'] = y_pred


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'MSE: {mse}')
print(f'R2 Score: {r2}')


plt.figure(figsize=(8, 5), dpi=300)
plt.scatter(y_test, y_pred, label='Predicted vs Actual', color='#E8E8E8')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='x=y')  


reg = LinearRegression().fit(y_test.values.reshape(-1, 1), y_pred)
y_fit = reg.predict(y_test.values.reshape(-1, 1))
plt.plot(y_test, y_fit, color='#E1B6B5', linewidth=3.0, label='Best fit line')



plt.xlabel('Observed lnCE')
plt.ylabel('Predicted lnCE')
plt.legend()
plt.savefig(r"真实值与预测值.svg")
plt.show()
