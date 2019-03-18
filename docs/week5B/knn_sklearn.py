import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

data = pd.read_csv('student.csv')
print(data.shape)
data.head()

math = data['Math'].values
read = data['Reading'].values
write = data['Writing'].values

# Ploting the scores as scatter plot
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(math, read, write, color='#ef1234')
# plt.show()

X = np.array([math, read]).T
Y = np.array(write)

X_train, X_test, y_train, y_test = train_test_split(
                                    X, Y, test_size=0.2, random_state=42)

# Model Intialization
reg = KNeighborsRegressor(n_neighbors=1)
# Data Fitting
reg = reg.fit(X_train, y_train)
# Y Prediction
Y_pred = reg.predict(X_test)

# Model Evaluation
rmse = np.sqrt(mean_squared_error(y_test, Y_pred))
r2_train = reg.score(X_train, y_train)
r2_test = reg.score(X_test, y_test)

# print("RMSE")
# print(rmse)
print("R2 Score Train: {}".format(r2_train))
print("R2 Score Test: {}".format(r2_test))