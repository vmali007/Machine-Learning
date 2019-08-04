import numpy as np
import pandas as pd

mse = [15,22,16,18,30]
ese = [55,68,62,65,72]

x = pd.Series(mse)
y = pd.Series(ese)

xm = x.mean()
ym = y.mean()

r = x.cov(y)/(x.std()*y.std())

beta1 = r*y.std()/x.std()
beta0 = ym - beta1*xm

print("coeff is :",beta1)
print("intercept is :",beta0)
while(1):
    x_in = int(input("enter the mse marks:" ))

    y_op = beta0 + beta1*x_in

    print("the ese marks are :",y_op)