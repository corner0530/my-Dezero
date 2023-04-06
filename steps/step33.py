# 33. ニュートン法を使った最適化(自動計算)
import numpy as np

from dezero import Variable


def f(x):
    y = x**4 - 2 * x**2
    return y


if __name__ == "__main__":
    x = Variable(np.array(2.0))
    iters = 10

    for i in range(iters):
        print(i, x)

        y = f(x)
        x.cleargrad()
        y.backward(create_graph=True)

        gx = x.grad
        x.cleargrad()
        gx.backward()
        gx2 = x.grad

        x.data -= gx.data / gx2.data
