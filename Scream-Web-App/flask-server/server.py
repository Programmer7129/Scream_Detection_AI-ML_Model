from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import numpy as np
from tensorflow import keras
import pandas as pd
from scipy.io.wavfile import read
import librosa
import pickle
import glob
from keras.models import Sequential
from keras.layers import Dense


app = Flask(__name__)
CORS(app)

# Members API route
@app.route("/members", methods=["POST"])
def members():
    if "file" not in request.files:
        return {"error": "No file uploaded"}, 400

    file = request.files["file"]
    if file.filename == "":
        return {"error": "No file selected"}, 400

    filename = secure_filename(file.filename)
    file_path = "uploads/" + filename
    file.save(file_path)  # Save the file to the "uploads" folder

    df = pd.read_csv('AI-stuff/newresources.csv', index_col=0, engine = 'c')
    file = open("AI-stuff/begining index of testing files.txt","r")
    data1 = int(file.read())
    file.close()
    row_num_for_verification_of_model = data1
    X = df.iloc[:row_num_for_verification_of_model,1:]  #independent variables columnns
    print(row_num_for_verification_of_model)
    X2 = df.iloc[row_num_for_verification_of_model:,1:]
    file = open("AI-stuff/input dimension for model.txt","r")
    data2 = int(file.read())
    file.close()
    print(data2)
    total_number_of_column_required_for_prediction = data2
    column_number_of_csv_having_labels = 0
    y = df.iloc[:data1,column_number_of_csv_having_labels] # dependent variable column
    # # define the keras model
    model = Sequential()
    model.add(Dense(12, input_dim=total_number_of_column_required_for_prediction, activation='relu'))
    model.add(Dense(8, activation='relu'))

    model.add(Dense(10, activation='relu'))
    model.add(Dense(5, activation='relu'))
    model.add(Dense(3, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # compile the keras model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # fit the keras model on the dataset
    history = model.fit(X, y,validation_split=0.33, epochs=150, batch_size=50

                        )


    # evaluate the keras model
    _, accuracy = model.evaluate(X, y)
    print('Accuracy: %.2f' % (accuracy * 100))

    # make probability predictions with the model
    predictions = model.predict(X2)

    # round predictions
    rounded = [round(x[0]) for x in predictions]

    print("predicted value is"+str(rounded))
    print("actual value was"+str(list(df.iloc[row_num_for_verification_of_model:,column_number_of_csv_having_labels])))

    model.save('.')
    output1 = svm_process(file_path) 
    print("model 1")
    print(output1)
    output2 = process_file(file_path)               # it will process file in multilayer perceptron model
    text = ""
    number_color = 0
    print("model 2")
    print(output2)
    if output1== True and output2 == True:
        pass    
        # call emergency funtion with higher risk currently we haven;t implemented emergency function
        text = "High"
        number_color = 2
        print(text)
    elif output1 == True or output2 == True:
        # call emergency function
        text = "Medium"
        number_color = 1
        print(text)
        pass
    else:
        text = 'you are safe'
        number_color = 0
        print("you are safe")

    return {"is_scream": text, "number_color": number_color}

def tetsting_unit(filename):
    tester = []
    import librosa 
    test, ans = librosa.load(filename)  # provide path of  wave file
    mfccs = np.mean(librosa.feature.mfcc(y=test, sr=ans, n_mfcc=40).T, axis=0)
    tester.append(mfccs)
    tester = np.array(tester)
    return tester #return Mfcss extracted arrray 

def process_file(filename):
    arr = []
    model = keras.models.load_model('.')
    print(filename)
    data, rs = read(filename)
    file = open("AI-stuff/input dimension for model.txt", "r")
    suitable_length_for_model = int(file.read())
    file.close()
    rs = rs.astype(float)
    rs = rs[0:suitable_length_for_model+1]
    a = pd.Series(rs.flatten())
    arr.append(a)
    df = pd.DataFrame(arr)
    X2 = df.iloc[0:, :48250]
    #print(X2)
    predictions = model.predict(X2)
    rounded = [round(x[0]) for x in predictions]

    #print("predicted value is" + str(rounded))
    if str(rounded)=='[1.0]':
        return True
    else:
        return False

def svm_process(filename):
    import pickle  # importing pickle to load saved model

    load_model = pickle.load(open('AI-stuff/phase1_model.sav', 'rb'))  # loading phase_1 model (noise vs speech)
    result = load_model.predict(tetsting_unit(filename))  # predicting if result[0]==1 then noise else human sound
    load_model2 = pickle.load(open('AI-stuff/phase2_model.sav', 'rb'))  # loading phase2 model
    if result[0] == 2:  # checking sound noise or human
        print("Phase-1 clear")
        ok = load_model2.predict(tetsting_unit(filename))  # using second phase_model
        if ok[0] == 1:
            # print("Phase-2 clear")
            # print('Scream')
            return True
        else:
            # print('speech')
            return False
    else:
        # print("noise")
        return "Noise"


# dataset for this model can be easily prepare by datasetmaker.py file


if  __name__ == "__main__":
    app.run(debug=True)
