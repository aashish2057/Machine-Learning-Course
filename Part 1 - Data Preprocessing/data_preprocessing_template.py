# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:58:58 2019

@author: aashi
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values