# 处理序列数据  NLP
# why  普通神经元只作用于预设的固定维度输入和输出，
# 而RNN支持输入输出可变长度序列
# 翻译-多对多、情感分析--多对一

# 天气 好还是不好. 多对一. 分类问题
#%%
from weatherData import train_data,test_data
# words
vocab = list(set([w for text in train_data.keys() for w in text.split(' ')]))
vocab_size = len(vocab)
# print(vocab)
# 词索引，枚举 w 为词，i为对应id
word_to_idx = {w: i for i, w in enumerate(vocab)}
idx_to_word = {i: w for i, w in enumerate(vocab)}
# 使用one-hot编码将x转成向量

import numpy as np

# 一个x会是多组one-hot编码懂的组合
def createInputs(text):
    inputs = []
    for w in text.split(' '):
        v = np.zeros((vocab_size,1))
        v[word_to_idx[w]] = 1
        inputs.append(v) 
    return inputs

class RNN:
    def __init__(self, input_size, output_size, hidden_size=64):
        self.Whh = np.random.randn(hidden_size, hidden_size) /1000
        self.Wxh = np.random.randn(hidden_size, input_size) / 1000
        self.Why = np.random.randn(output_size, hidden_size) / 1000

        self.bh = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))

    def forward(self, inputs):
        # 初始化
        h = np.zeros((self.Whh.shape[0],1))

        self.last_inputs = inputs
        self.last_hs = {0:h}

        for i, x in enumerate(inputs):
            h = np.tanh(self.Wxh @ x + self.Whh @ h + self.bh)
            self.last_hs[i+1] = h
        y = self.Why @ h + self.by
        return y, h
    
    def backprop(self, d_y, learn_rate=2e-2):
        # BPTT
        n = len(self.last_inputs)
        d_Why = d_y @ self.last_hs[n].T
        d_by = d_y

        d_Whh = np.zeros(self.Whh.shape)
        d_Wxh = np.zeros(self.Wxh.shape)
        d_bh = np.zeros(self.bh.shape)
        d_h = self.Why.T @ d_y

        for t in reversed(range(n)):
            temp = ((1 - self.last_hs[t + 1] ** 2) * d_h)
            d_bh += temp
            d_Whh += temp @ self.last_hs[t].T
            d_Wxh += temp @ self.last_inputs[t].T

        for d in [d_Wxh, d_Whh, d_Why, d_bh, d_by]:
            np.clip(d ,-1, 1, out=d)
        self.Whh -= learn_rate * d_Whh
        self.Wxh -= learn_rate * d_Wxh
        self.Why -= learn_rate * d_Why
        self.bh -= learn_rate * d_bh
        self.by -= learn_rate * d_by
    
def softmax(xs):
    return np.exp(xs) / sum(np.exp(xs))

rnn = RNN(vocab_size,2)
inputs = createInputs('i am very good')
out, h = rnn.forward(inputs)
probs = softmax(out)
print(f"probs {probs}")



import random

def processData(data, backprop=True):
    items = list(data.items())
    random.shuffle(items)

    loss = 0 
    num_correct = 0
    for x, y in items:
        inputs = createInputs(x)
        target = int(y)

        out, _ = rnn.forward(inputs)
        probs = softmax(out)

        loss -= np.log(probs[target])
        num_correct += int(np.argmax(probs) == target)

        if backprop:
            d_L_d_y = probs
            d_L_d_y[target] -= 1

            rnn.backprop(d_L_d_y)
    return loss / len(data), num_correct / len(data)

# Training loop
for epoch in range(1000):
  train_loss, train_acc = processData(train_data)

  if epoch % 100 == 99:
    print('--- Epoch %d' % (epoch + 1))
    print('Train:\tLoss %.3f | Accuracy: %.3f' % (train_loss, train_acc))

    test_loss, test_acc = processData(test_data, backprop=False)
    print('Test:\tLoss %.3f | Accuracy: %.3f' % (test_loss, test_acc))

# %%
