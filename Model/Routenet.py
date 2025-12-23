import tensorflow as tf
from tensorflow import keras 
import numpy as np
import argparse

from Model.Hyperparameters import hyperparameters

hyperparameters=hyperparameters()

class RouteNet(keras.Model):
    def __init__(self,hyperparameters):
        super(RouteNet,self).__init__()
        self.hyperparameters=hyperparameters


if __name__ == "__main__":
    print("RouteNet model file")
