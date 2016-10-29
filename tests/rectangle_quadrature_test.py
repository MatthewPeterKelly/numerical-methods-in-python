#!/usr/bin/env python

from numerical_methods import RectangleQuadrature
from numerical_methods import HelloWorld


def test_function(x):
    return x*x


def main():
    """
    Demonstrates how to use rectangle quadrature to compute the integral of
    x^2 on the domain [0,1]. Compute the solution for a a range of different
    segment counts.
    """
    quad = RectangleQuadrature(test_function, 0.0, 1)
    for n in [1,2,4,8,16,32,64,128, 256, 512]:
        quad.create_uniform_segments(n)
        print 'J = ' + str(quad.evaluate()) + '  (' + str(n) +' segments)'
    print 'J = 0.3333333333333  (analytic solution)'

if __name__ == "__main__":
    main()
