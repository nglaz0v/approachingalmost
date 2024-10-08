#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DL model.
"""

import torch.nn as nn
import pretrainedmodels


def get_model(pretrained):
    MODEL_NAME = "resnet18"  # "alexnet"
    if pretrained:
        model = pretrainedmodels.__dict__[MODEL_NAME](
            pretrained='imagenet'
        )
    else:
        model = pretrainedmodels.__dict__[MODEL_NAME](
            pretrained=None
        )
    # print the model here to know whats going on.
    # model.last_linear = nn.Sequential(
    #     nn.BatchNorm1d(4096),
    #     nn.Dropout(p=0.25),
    #     nn.Linear(in_features=4096, out_features=2048),
    #     nn.ReLU(),
    #     nn.BatchNorm1d(2048, eps=1e-05, momentum=0.1),
    #     nn.Dropout(p=0.5),
    #     nn.Linear(in_features=2048, out_features=1),
    # )
    model.last_linear = nn.Sequential(
        nn.BatchNorm1d(512),
        nn.Dropout(p=0.25),
        nn.Linear(in_features=512, out_features=2048),
        nn.ReLU(),
        nn.BatchNorm1d(2048, eps=1e-05, momentum=0.1),
        nn.Dropout(p=0.5),
        nn.Linear(in_features=2048, out_features=1),
    )
    return model
