# encoding: utf-8
# Author    : WuY<wuyong@mails.ccnu.edu.com>
# Datetime  : 2023/10/21
# User      : WuY
# File      : utils.py
# 将各种用于神经网络的`一些工具`集合到这里

import os
import sys
sys.path.append(os.path.dirname(__file__))  # 将文件所在地址放入系统调用地址中
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

# Dacay learning_rate
def lr_scheduler(optimizer, epoch, init_lr=0.01, lr_decay_epoch=40):
    """Decay learning rate by a factor of 0.1 every lr_decay_epoch epochs."""
    lr = init_lr*(0.1**(epoch // lr_decay_epoch))
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

# 将标签转化为one-hot
def toOneHot(labels, num_class=10):
    batch_size = labels.view(-1).shape[0]
    labels_ = torch.zeros(batch_size, num_class).scatter_(1, labels.view(-1, 1), 1)
    return labels_

# 使用输出和标签值(非one-hot)得到，总数和正确数
def calc_correct_total(outputs, labels):
    """
    args:
        :param outputs: 网络输出值
        :param labels: 标签值
    return:
        :param total: 标签总数
        :param correct: 输出正确数
    """
    _, predicted = outputs.cpu().max(1) # max()输出(值，索引)
    labels = labels.view(-1)
    total = float(labels.size(0)) # 输出标签总数
    correct = float(predicted.eq(labels).sum().item()) # 输出正确数
    return total, correct


