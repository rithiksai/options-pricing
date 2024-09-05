import math
from statistics import NormalDist
import streamlit as st



#code for creating a UI using streamlit
s = st.number_input("Enter the stock price : ")
x = st.number_input("Enter the strike price : ")
r = st.number_input("Enter the interest rate : ")
t = st.number_input("Enter the time to expiration : ")
sigma = st.number_input("Enter the volatility : ")



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



nd1 = NormalDist(mu=0, sigma=1).cdf(d1)
nd2 = NormalDist(mu=0, sigma=1).cdf(d2)


z = r*t
c = (s*nd1)- (x*math.exp(-z)*nd2)

st.write("THE PRICE OF THE EUROPEAN CALL OPOTION : ",c)
