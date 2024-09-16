#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This will create a new file in the input/ folder called adult_folds.csv,
and it’s the same as adult.csv. The only differences are that this CSV is
 shuffled and has a new column called kfold. (Each sample is assigned a value
from 0 to k-1 when using stratified k-fold cross validation.)
"""

# import pandas and model_selection module of scikit-learn
import pandas as pd
from sklearn import model_selection


if __name__ == "__main__":

    # Read training data
    df = pd.read_csv("../input/adult.csv")

    # we create a new column called kfold and fill it with -1
    df["kfold"] = -1

    # the next step is to randomize the rows of the data
    df = df.sample(frac=1).reset_index(drop=True)

    # fetch labels
    y = df.income.values

    # initiate the kfold class from model_selection module
    kf = model_selection.StratifiedKFold(n_splits=5)

    # fill the new kfold column
    for f, (t_, v_) in enumerate(kf.split(X=df, y=y)):
        df.loc[v_, 'kfold'] = f

    # save the new csv with kfold column
    df.to_csv("../input/adult_folds.csv", index=False)