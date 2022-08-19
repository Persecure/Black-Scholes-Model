# Black Scholes Model

The Black-Scholes model is used to determine the fair price or theoretical value of a call or put option based on certain variables. This code will showcase a simple python program utilizing various modules to calculate the Black-Scholes pricing model. The inputs of the variables can be changed in the "Test" variable. 

![image](https://user-images.githubusercontent.com/93418272/180991444-cded48dd-e524-443f-8e0f-8a52b29dda1d.png)

Breaking down the imported module functions:

np.log(x) = ln() 
functionsi.norm.cdf = Cumulative normal distribution function

math.exp = Return 'E' raised to the power of

Changes inputs in decimales:

rf = rf / 100

q = q / 100

vol = vol / 100


#!/usr/bin/env python
import math
import numpy as np
import scipy.stats as si
import math

def BlackScholes(S,K,T,rf,q,vol):
    """
        S = Stock price
        K = Strike price
        T = Time to maturity in years
        rf = Risk-free rate
        q = dividen rate
        vol = volatility (standard deviation)
    """
    rf = rf / 100
    q = q / 100
    vol = vol / 100

    d1 = ((np.log(S/K)) + ((rf+0.5*vol**2)*T)) / (vol*(T**0.5))
    Nd1 = si.norm.cdf(d1,0.0,1.0)

    d2 = d1 - (vol*(T**0.5))
    Nd2 = si.norm.cdf(d2,0.0,1.0)

    Call = (S*Nd1) - (K*(math.exp(-rf*T))*Nd2)
    
    return Call
    


Test = BlackScholes(100,100,(30/365),5,0,25)
print(Test)
