import pandas as pd
df = pd.read_csv('https://github.com/akiwelekar/MLModels/blob/master/aimarks2017.csv')
x = df["mse"]
y = df["ese"]
def gradiant(x,y,inp):
    n = float(len(x))
    m = 0
    c = 0
    y_pre = 0
    lr = 0.00001
    for i in range(10000):
        y_pre = x * m + c
        dm = (-2/n)*sum(x*(y - y_pre))
        dc = (-2/n)*sum(y - y_pre)
        m = m - lr*dm
        c = c - lr*dc
    print(f"slope = {m} constant = {c} ")
    op = m * inp + c
    print(op)

def ordinary(x,y,inp):
    _x = pd.Series(x)
    _y = pd.Series(y)
    x_mean = _x.mean()
    y_mean = _y.mean()
    
    r = _x.cov(_y)/(_x.std()*_y.std())
    m2 = r*_y.std()/_x.std()
    c2 = y_mean - m2*x_mean
    print(f'slope = {m2} constant = {c2}')
    op2 = m2*inp + c2
    print(op2)

inp = int(input())
gradiant(x,y,inp)
ordinary(x,y,inp)