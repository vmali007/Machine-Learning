import pandas as pd
x = pd.Series([15,12,8,8,7,7,7,6,5,3])
y = pd.Series([10,25,17,11,13,17,20,13,9,15])

r = x.cov(y)/(x.std()*y.std())

beta1 = r*y.std()/x.std()

print("%.3f"%beta1)