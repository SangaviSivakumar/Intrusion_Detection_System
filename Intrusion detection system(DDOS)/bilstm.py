from tensorflow.keras.models import *
from tensorflow.keras.layers import *

def bilstm_layer(lstm_dt, layer):
    bilstm_struct = Dense(layer,activation='relu')
    return bilstm_struct

