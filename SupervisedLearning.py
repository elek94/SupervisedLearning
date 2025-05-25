import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Salary.csv')
print(data.head())

x = data['YearsExperience']
y = data['Salary']

plt.figure(figsize=(12,5))
plt.scatter(x,y, s=300, c='g', marker=r'$\clubsuit$')
plt.xlabel('Years of experience')
plt.ylabel('Salary')

def linear_regression(x, y):
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()
    
    a_num = ((x - x_mean) * (y - y_mean)).sum()
    a_den = ((x - x_mean)**2).sum()
    a = round(a_num / a_den, 3)
    
    b = round(y_mean - (a*x_mean),3)
    
    reg_line = 'y = {} + {}x'.format(b,a)
    
    return (b, a, reg_line)

(b, a, line) = linear_regression(x, y)
print(b)

def predict(b, a, new_x):
    y = b + a * new_x
    return y

predict(b, a, 24)