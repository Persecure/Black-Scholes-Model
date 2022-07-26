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
