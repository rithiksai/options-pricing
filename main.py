import math
from statistics import NormalDist


s = float(input("Enter the stock price : "))
x = float(input("Enter the strike price : "))
r = float(input("Enter the interest rate : "))
t = float(input("Enter the time to expiration : "))
sigma = float(input("Enter the volatility : "))

def calcd1(s,x,r,t,sigma):
    a =  math.log(s/x)
    b = (sigma**2/2) + r
    c = sigma*math.sqrt(t)
    d1 = (a + b*t)/c
    return d1

def calcd2(d1,sigma,t):
    
    d2 = d1 - (sigma*math.sqrt(t))
    return d2

d1 =calcd1(s,x,r,t,sigma)
d2 = calcd2(d1,sigma,t)
print(d1)
print(d2)


nd1 = NormalDist(mu=0, sigma=1).cdf(d1)
nd2 = NormalDist(mu=0, sigma=1).cdf(d2)

print(nd1)
print(nd2)

z = r*t
c = (s*nd1)- (x*math.exp(-z)*nd2)

print("THE PRICE OF THE EUROPEAN CALL OPOTION : "+ str(c))
