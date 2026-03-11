import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

data = {
    'X1': [1,2,3,4,5],
    'X2': [2,1,4,3,5],
    'Y':  [2,3,5,7,11]
}

df = pd.DataFrame(data)

X_simple = df[['X1']]
X_multiple = df[['X1','X2']]
y = df['Y']

model_simple = LinearRegression()
model_simple.fit(X_simple,y)
pred_simple = model_simple.predict(X_simple)

model_multiple = LinearRegression()
model_multiple.fit(X_multiple,y)
pred_multiple = model_multiple.predict(X_multiple)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_simple)

model_poly = LinearRegression()
model_poly.fit(X_poly,y)
pred_poly = model_poly.predict(X_poly)

def evaluate(y_true,y_pred):
    r2 = r2_score(y_true,y_pred)
    mae = mean_absolute_error(y_true,y_pred)
    rmse = np.sqrt(mean_squared_error(y_true,y_pred))
    return r2,mae,rmse

print("Simple Linear Regression:", evaluate(y,pred_simple))
print("Multiple Linear Regression:", evaluate(y,pred_multiple))
print("Polynomial Regression:", evaluate(y,pred_poly))