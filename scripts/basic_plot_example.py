#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Draw a simple plot of a sine curve
    """

    t = np.arange(0.0, 2.0, 0.01)
    s = np.sin(2*np.pi*t)
    plt.plot(t, s)

    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()


if __name__ == "__main__":
    main()
