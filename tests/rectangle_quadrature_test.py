#!/usr/bin/env python

from numerical_methods import RectangleQuadrature
from numerical_methods import HelloWorld

def test_function(x):
    return x*x

def main():

    hello_world = HelloWorld()
    hello_world.print_text()

    quad = RectangleQuadrature(test_function, 0.0, 1.0)
    print quad.evaluate()


if __name__ == "__main__":
    main()
