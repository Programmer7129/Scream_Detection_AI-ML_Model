from sklearn import svm
import numpy as np
from sklearn import mixture
from numpy import genfromtxt
import pandas as pd
from sklearn.metrics import accuracy_score

def tetsting_unit( ):
    tester = []
    import librosa
    test, ans = librosa.load("D:/Dev_stuff/audio_dataset/")
    mfccs = np.mean(librosa.feature.mfcc(test, ans, n_mfcc=40).T, axis=0)
    tester.append(mfccs)
    tester = np.array(tester)
    return tester


x_train = genfromtxt('datasets/modified_data.csv', delimiter=',')
y_train = genfromtxt('datasets/solution.csv',delimiter=',')
#print(x_train.shape, y_train.shape)
clf = svm.SVC(kernel="linear")
clf.fit(x_train, y_train)
prd=clf.predict(tetsting_unit())
if prd[0] == 2:
    print("phase 1 clear")
    import phase2_speech_vs_high_pitch as sf
    ok = sf.second_para.predict(tetsting_unit())
    if ok[0] == 1:
        print('scream')
    else:
        print('speech')
else:
    print("noise")
