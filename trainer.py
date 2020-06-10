""" training script """

import pandas as pd
import numpy as np
import argparse
import tensorflow as tf

import data_helpers as dh

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Model Training Script")
    parser.add_argument('key', help='User API Key')
    parser.add_argument('-outdir', metavar='out', default='/models/', help="Directory for stored model(s) (one for each symbol).")
    parser.add_argument('symbols', nargs=argparse.REMAINDER, help="List of symbols to train (Place all at end of command)")
    parse = parser.parse_args()

    data = {}

    for symbol in parse.symbols:

        # read historical daily data from alpha_vantage
        # store in python dict
        hist = dh.daily(symbol, parse.key, compact=False)
        data[symbol] = hist
        #print(hist)
        #print()

        """ Data Preprocessing """ 

        # turn dataframe to numpy array
        tmp = hist.to_numpy()

        # split into training and testing sets 90-10
        split = round(tmp.shape[0]*1/10)
        test, training = tmp[:split], tmp[split:]
        #print(training.shape)
        #print(test.shape)

        # convert numpy arrays to PyTorch tensors
        training_tensor = tf.convert_to_tensor(training, np.float32)
        test_tensor = tf.convert_to_tensor(test, np.float32)
        
        """ -------------------------------- """
        print(training_tensor)
        print(test_tensor)