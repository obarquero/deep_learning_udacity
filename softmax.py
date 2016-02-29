# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:21:31 2016
Softmax exercise:

Wikipedia definition: In mathematics, in particular probability theory and 
related fields, the softmax function, or normalized exponential,[1]:198 is a 
generalization of the logistic function that "squashes" a K-dimensional vector 
\mathbf{z} of arbitrary real values to a K-dimensional vector
 \sigma(\mathbf{z}) of real values in the range (0, 1) that add up to 1. 
The function is given by
@author: obarquero
"""
"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    
    return np.exp(x)/np.sum(np.exp(x),axis = 0)

    #pass  # TODO: Compute and return softmax(x)


print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()