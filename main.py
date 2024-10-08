import math
from statistics import NormalDist
import streamlit as st

st.title(":sunglasses: :blue[call] and :green[put] option price calculator")
#code for creating a UI using streamlit
s = st.number_input("Enter the stock price : ",value = 1)
x = st.number_input("Enter the strike price : ",value=1)
r = st.number_input("Enter the interest rate : ",value = 0.01)
t = st.number_input("Enter the time to expiration : ",value = 1)
sigma = st.number_input("Enter the volatility : ",value = 0.1)

#this is a test change made from another workstation


if st.button("Calculate"):
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


    #Calculation for call option pricing
    nd1 = NormalDist(mu=0, sigma=1).cdf(d1)
    nd2 = NormalDist(mu=0, sigma=1).cdf(d2)
    z = r*t
    c = (s*nd1)- (x*math.exp(-z)*nd2)

    #calculation for put option pricing
    pd1 =NormalDist(mu=0, sigma=1).cdf(-d1)
    pd2 = NormalDist(mu=0, sigma=1).cdf(-d2)
    p = (x*math.exp(-z)*pd2) - s*pd1    


    font_size = 30

    html_str = f"""
    <style>
    p.a {{
    font: bold {font_size}px Courier;
    color:green;
    
    }}
    p.b{{
    font: bold {font_size}px Courier;
    color:blue;
    
    }}
    </style>
    <p class="a">CALL : {c}</p>
    <p class="b">PUT : {p}</p>
    """

    st.markdown(html_str, unsafe_allow_html=True)


