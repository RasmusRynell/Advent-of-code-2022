import json
import sys
import os
#import torch
import numpy as np
import matplotlib.pyplot as plt
import time

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input_test.txt'), 'r') as f:
        blueprints = f.read().splitlines()

    print(blueprints)