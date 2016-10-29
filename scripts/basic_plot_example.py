#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

# EXAMPLE FROM:  http://matplotlib.org/examples/pylab_examples/simple_plot.html


def curvy_function(t):
    return t*np.sin(2*np.pi*t) + 0.2*np.cos(7*np.pi*t)


def main():
    """
    Draw an interesting function
    """

    t = np.linspace(0.0, 1.0, 50)
    s = curvy_function(t)
    plt.plot(t, s)

    plt.xlabel('time (s)')
    plt.ylabel('position (m)')
    plt.title('a curvy plot!')
    plt.grid(True)
    # plt.savefig("curvy_plot.png")
    plt.show()


if __name__ == "__main__":
    main()
