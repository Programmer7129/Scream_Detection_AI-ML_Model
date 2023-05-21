# Scream_Detection_AI-ML_Model
This program uses a deep-neural network to detect the scream and take immediate actions to send help. 

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Scream Detection AI/ML Model is an innovative system developed to enhance the safety and security of our college community. The project aims to detect distress calls and screams in real-time, enabling immediate response and providing assistance to individuals in danger. This repository contains the source code and documentation related to the development and evaluation of the AI/ML model.

## Features
- Accurate detection of distress calls and screams
- Real-time response system
- Multi-layer perceptron (MLP) model for classification
- Support vector machines (SVM) for additional confirmation
- Visualizations for performance analysis
- Easy integration with specified locations in the community


## Usage
1. Prepare the dataset:
- Collect audio samples of distress calls, screams, and background noise.
- Organize the samples in the `resources` folder.
- Update the `newresources.csv` file with the appropriate labels.

2. Train the AI/ML model:
- Run the `train_model.py` script to train the multi-layer perceptron model.
- The model will be saved as a file for future use.

3. Evaluate the model:
- Run the `evaluate_model.py` script to assess the model's performance.
- The script generates visualizations, including training loss, accuracy, confusion matrix, audio waveform, spectrogram, and precision-recall curve.

4. Integration:
- Install the model in specified locations within the community for real-time scream detection.
- Use the `process_file()` and `svm_process()` functions in the code to process audio files and detect distress calls.

## Results
The project has demonstrated promising results in accurately detecting distress calls and screams. The AI/ML model achieved high accuracy and has been validated through extensive training and evaluation. The visualizations provide insights into the model's performance, helping assess its effectiveness.

![Training Loss and Accuracy](training_loss_accuracy.png)
![Confusion Matrix](confusion_matrix.png)
![Audio Waveform](audio_waveform.png)
![Spectrogram](spectrogram.png)
![Precision-Recall Curve](precision_recall_curve.png)

## Contributing
Contributions are welcome! If you have any ideas or suggestions to enhance the project, please feel free to open an issue or submit a pull request. Let's collaborate to make our community safer together.

## License
This project is licensed under the [MIT License](LICENSE).


