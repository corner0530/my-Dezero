# 40. ブロードキャストを行う関数
import numpy as np

from dezero import Variable

if __name__ == "__main__":
    x0 = Variable(np.array([1, 2, 3]))
    x1 = Variable(np.array([10]))
    y = x0 + x1
    print(y)

    y.backward()
    print(x1.grad)
