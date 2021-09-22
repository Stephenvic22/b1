import pandas 
import matplotlib.pyplot as plt
from matplotlib import pyplot

import random
import numpy as np

df = pandas.read_csv("data_linear.csv")

s = df['Diện tích'] 
g = df["Giá"] 
pyplot.plot(s,g, color = 'red', linestyle = '--', marker = '.')
pyplot.show()