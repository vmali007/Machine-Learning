import pandas as pd

m = pd.read_csv("https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt")
df = pd.DataFrame(m)
x = pd.Series(df["2.81"])
y = pd.Series(df["5.62"])

r = x.cov(y)/(x.std()*y.std())

b1 = r*y.std()/x.std()

b0 = y.mean() - (b1*x.mean())

inp = float(input())

y_pre = b0 + (inp * b1)

print("%.2f"%y_pre)
