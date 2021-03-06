import matplotlib.pyplot as plt
import numpy as np


def axisSetUp():
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))


def buildSmooth(f, Xn, Fxn, order):
    axisSetUp()

    t1 = np.arange(Xn[0], Xn[-1], 0.1)
    plt.plot(t1, f(t1, Xn, Fxn, order))

    for i_x, i_y in zip(Xn, f(Xn, Xn, Fxn, order)):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

    plt.show()


def buildInterpolated(f, Xn, Fxn):
    axisSetUp()

    t1 = np.arange(Xn[0], Xn[-1], 0.1)
    plt.plot(t1, f(t1, Xn, Fxn))

    for i_x, i_y in zip(Xn, f(Xn, Xn, Fxn)):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

    plt.show()


def build(Xn, Fxn):
    axisSetUp()

    plt.plot(Xn, Fxn)

    for i_x, i_y in zip(Xn, Fxn):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

    plt.show()
