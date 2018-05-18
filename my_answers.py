import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Activation
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []
    for i in range(0,len(series)-window_size-1):
        X.append(series[i:i+window_size])
        y.append([series[i+window_size]])
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5,return_sequences=True,input_shape=(window_size,1)))
    model.add(LSTM(1))
    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    s = ""
    for i in range(0,len(text)):
        if text[i] in punctuation or (text[i] >= 'a' and text[i] <= 'z'):
            s += text[i]
        else:
            s += ' '
    return s

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    for i in range(0,len(text)-window_size-1,step_size):
        inputs.append(text[i:i+window_size])
        outputs.append(str(text[i+window_size]))
    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
#     Time to get to work: build a 3 layer RNN model of the following specification
# layer 1 should be an LSTM module with 200 hidden units --> note this should have input_shape = (window_size,len(chars)) where len(chars) = number of unique characters in your cleaned text
# layer 2 should be a linear module, fully connected, with len(chars) hidden units --> where len(chars) = number of unique characters in your cleaned text
# layer 3 should be a softmax activation ( since we are solving a multiclass classification)
# Use the categorical_crossentropy loss
    
    model = Sequential()
    model.add(LSTM(200,input_shape=(window_size,num_chars)))
    model.add(Dense(num_chars))
    model.add(Activation('softmax'))
    return model
