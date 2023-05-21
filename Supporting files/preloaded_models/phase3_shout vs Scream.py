from sklearn import svm
import numpy as np
from numpy import genfromtxt
import pandas as pd
from sklearn.metrics import accuracy_score
import pickle
x_train = genfromtxt('pathlocation of csv',delimiter=',')
y_train = genfromtxt('id_of_it  csv',delimiter=',')
third_para = svm.SVC(kernel='linear',C=20.0,gamma=0.00001)
third_para.fit(x_train, y_train)