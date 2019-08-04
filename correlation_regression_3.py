import pandas as pd
x = pd.Series([15,12,8,8,7,7,7,6,5,3])
y = pd.Series([10,25,17,11,13,17,20,13,9,15])

x_mean = x.mean()
y_mean = y.mean()

r = x.cov(y)/(x.std()*y.std())

beta_1 = r*y.std()/x.std()

beta_0 = y_mean - x_mean*beta_1

case  = beta_0 + 10*beta_1

print("%.1f"%case)
