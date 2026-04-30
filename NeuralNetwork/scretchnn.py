# https://victorzhou.com/blog/intro-to-neural-networks/
#%%
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 一个神经元
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)
    
weights = np.array([0, 1])
bias = 4
n = Neuron(weights, bias)
x = np.array([2,3])
print(n.feedforward(x))

#%%。一个神经网络，含3个神经元
class NN:
    def __init__(self):
        weights = np.array([0,1])
        bias = 0

        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)
    
    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1
network = NN()
x = np.array([2,3])
print(network.feedforward(x))

#%%
# 定义损失函数
# mse y真实值 一般适用于one-hot编码，也就是分类任务，只有一个1，其余都为0，所以 Loss = (1 - y_pred)**2 。再对参数取偏微分的时候就可以用链式法则。偏微分求w权重时又可以看成反向传播。
def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

y_true = np.array([1,0,0,1])
y_pred = np.array([0,0,0,0])
print(mse_loss(y_true,y_pred)) 
# 随机梯度下降
#%% 完整的神经网络

import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def deriv_sigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)
def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) **2 ).mean()

class NeuralNetwork:
    def __init__(self):
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()
    def fp(self, x):
        #  ypred <-- o1 <-- h1 + h2 <-- x1 + x2
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    def train(self, data, all_y_trues):
        learn_rate = 0.1
        epochs = 1000

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # 依旧先加权再sigmoid FP
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_h1)
                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)
                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                y_pred = o1
                # BP
                d_L_d_pred = -2 * (y_true - y_pred)
                # o1
                d_ypred_d_w6 = h1 * deriv_sigmoid(sum_o1)
                d_ypred_d_w5 = h2 * deriv_sigmoid(sum_o1)
                d_ypred_d_b3 = deriv_sigmoid(sum_o1)

                d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)
                # h1
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
                d_h1_d_b1 = deriv_sigmoid(sum_h1)

                d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)
                d_h2_d_b2 = deriv_sigmoid(sum_h2)
                # . 权重更新方式为 w = x * 偏导
                self.w1 -= learn_rate * d_L_d_pred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_pred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_pred * d_ypred_d_h1 * d_h1_d_b1
                self.w3 -= learn_rate * d_L_d_pred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_pred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_pred * d_ypred_d_h2 * d_h2_d_b2
                self.w5 -= learn_rate * d_L_d_pred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_pred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_pred * d_ypred_d_b3
            if epoch % 10 == 0:
                y_preds = np.apply_along_axis(self.fp, 1, data)
                loss = mse_loss(all_y_trues, y_preds)
                print("Epoch %d loss: %.3f" % (epoch, loss))
data = np.array([
  [-2, -1],  # Alice
  [25, 6],   # Bob
  [17, 4],   # Charlie
  [-15, -6], # Diana
])
all_y_trues = np.array([
  1, # Alice
  0, # Bob
  0, # Charlie
  1, # Diana
])
nn = NeuralNetwork()
nn.train(data, all_y_trues)

                





        
# %%

