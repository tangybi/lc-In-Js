# https://iamtrask.github.io/2015/07/12/basic-python-network/

import numpy as np

X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])

y = np.array([[0,1,1,0]]).T
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
for j in range(60000):
    # sigmoid function
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    # gap
    l2_delta = (y - l2)*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    # refresh weights
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)
print("Output After Training:")
print(l2)
#%%
#  linear algebra library 线性代数库
import numpy as np
# 非线性函数 nonlinearity。sigmoid  
def nonlin(x,deriv=False):
    # 求导，sigmoid的特性就是输出可以用来创建其导数，很重要
    # y‘ = y * (1-y)
    if(deriv == True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
# 4行3列，输入为3个特征 ，4个样本
X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
# 输出  4行1列，4个样本的输出。因此，神经网络就是3个输入1个输出
y = np.array([[0],[0],[1],[1]])

# 随机种子，以同样的方式生成随机数
np.random.seed(1)
# 权重矩阵，已有2层：输入层、输出层。 随机 0-1 均匀分布，均值为0（权重初始化） 。神经网络指此矩阵，所有的训练都被保存在这个矩阵里。
# 连接层的维度 3 * 1，输入层的特征数为3，输出层的特征数为1
# synapse zero 神经突触
syn0 = 2*np.random.random((3,1)) - 1
# 开始训练，迭代10000次
for iter in range(10000):
    # 第一层，4个样本同时执行，全批量训练 "full batch" training
    l0 = X
    # 前向预测，dot是矩阵乘法，sigmoid函数 sigmoid(x*w)  4*1
    l1 = nonlin(np.dot(l0,syn0))
    # 得到实际值和预测值的偏差，斜率都在0-1之间
    l1_error = y - l1
    # 梯度下降方式更新权重 4*1 
    l1_delta = l1_error * nonlin(l1,True)
    # 3*1 = 3*4 dot 4*1 得到更新权重 w1 = w0 + 输入值*偏差*导数
    syn0 += np.dot(l0.T,l1_delta)
print("Output After Training:")
print(l1)
#%%  3层，注意l2层更新权重的方式

w_1 = 2 * np.random.random((3,4)) - 1
w_2 = 2 * np.random.random((4,1)) - 1
for iter in range(10000): 
    l0 = X
    l1 = nonlin(np.dot(X, w_1)) 
    l2 = nonlin(np.dot(l1, w_2))

    l2_err = y - l2
    l2_del = l2_err * nonlin(l2,deriv=True)
    # BP：利用第二层的置信加权误差，为第一层计算误差。将误差沿着权重反向传播到第一层。--网络不变，输入从x转向l2_del 可知l1中每个节点对l2误差分别做了多大贡献。
    l1_err = l2_del.dot(w_2.T)
    l1_del = l1_err * nonlin(l1, deriv=True)

    w_2 += l1.T.dot(l2_del)
    w_1 += l0.T.dot(l1_del)
print("Output After Training:")
print(l2)

#%% 4层

import numpy as np
X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0]]).T
np.random.seed(1)
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
syn2 = 2*np.random.random((1,1)) - 1
for j in range(60000):
    # FP
    l0 = X
    l1 = 1/(1+np.exp(-(np.dot(l0,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    l3 = 1/(1+np.exp(-(np.dot(l2,syn2))))
    # BP
    l3_error = y - l3
    # 误差先加权再sigmoid。 斜率还是输出值的斜率
    l3_delta = l3_error * nonlin(l3, deriv=True)
    # 加权
    l2_error = l3_delta.dot(syn2.T)
    l2_delta = l2_error * nonlin(l2)

    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1,deriv=True)

    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)
print("Output After Training:")
print(l3)

