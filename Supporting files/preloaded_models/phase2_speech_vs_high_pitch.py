from sklearn import svm
import numpy as np
from numpy import genfromtxt
import pandas as pd
from sklearn.metrics import accuracy_score
x_train = genfromtxt('speech.csv',delimiter=',')
y_train = genfromtxt('id_of_it.csv',delimiter=',')
second_para = svm.SVC(C=20.0,gamma=0.00001)
second_para.fit(x_train, y_train)
