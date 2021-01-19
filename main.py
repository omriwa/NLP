import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd

# Dataset
dataset = pd.read_csv("Restaurant_Reviews.tsv",delimiter="\t",quoting=3)
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

# Splitting the dataset to training and test set
from sklearn.model_selection import train_test_split
