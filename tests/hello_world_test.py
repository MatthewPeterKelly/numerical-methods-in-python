#!/usr/bin/env python

from numerical_methods import HelloWorld
import argparse


def main():
    """
    Runs a simple test of the HelloWorld class.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text',
                        help='optional text string to echo')
    args = parser.parse_args()

    if args.text is not None:
        hello_world = HelloWorld(args.text)
    else:
        hello_world = HelloWorld()

    hello_world.print_text()


if __name__ == "__main__":
    main()
