import chainer.functions as CF
import numpy as np
import pytest

import dezero.functions as F
from dezero import Variable
from dezero.utils import array_allclose, gradient_check


def test_forward1():
    x = np.array([[0, 1, 2], [0, 2, 4]], np.float32)
    y2 = CF.sigmoid(x)
    y = F.sigmoid(Variable(x))
    res = array_allclose(y.data, y2.data)
    assert res


def test_forward2():
    x = np.random.randn(10, 10).astype(np.float32)
    y2 = CF.sigmoid(x)
    y = F.sigmoid(Variable(x))
    res = array_allclose(y.data, y2.data)
    assert res


def test_backward1():
    x_data = np.array([[0, 1, 2], [0, 2, 4]])
    assert gradient_check(F.sigmoid, x_data)


def test_backward2():
    np.random.seed(0)
    x_data = np.random.rand(10, 10)
    assert gradient_check(F.sigmoid, x_data)


def test_backward3():
    np.random.seed(0)
    x_data = np.random.rand(10, 10, 10)
    assert gradient_check(F.sigmoid, x_data)


if __name__ == "__main__":
    pytest.main()
