#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download MNIST dataset.
"""

import os
import pandas as pd
import numpy as np
from sklearn import datasets


if __name__ == "__main__":
    if not os.path.exists("../input"):
        os.mkdir("../input")

    data = datasets.fetch_openml(
        'mnist_784',
        version=1,
        return_X_y=True
    )
    pixel_values, targets = data
    targets = targets.astype(int)
    pixel_values = pixel_values.values

    mnist = pd.DataFrame(
        np.column_stack((targets, pixel_values)),
        columns=["label"] + [f"{n//28+1}x{n%28+1}" for n in range(pixel_values.shape[1])]
    )

    mnist.to_csv("../input/mnist_train.csv")
