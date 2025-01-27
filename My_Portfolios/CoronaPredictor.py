import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomidalFeatures


#### Load Data ####
data = pd.read_csv('D:\Angela-Learn-Python\My_Portfolios\VNcase.csv', sep = ',')
data = data[['id','cases']]
print('-'*30);print('HEAD');print('-'*30)
print(data.head())


#### Prepare Data ####
print('-'*30);print('Prepare Data');print('-'*30)
x = np.array(data['id']).reshape(-1, 1)
y = np.array(data['cases']).reshape(-1, 1)
plt.plot(y, '-m')
plt.show()

polyFeat = PolynomidalFeatures(degree=2)
x = polyFeat.fit_transform(x)
print(x)