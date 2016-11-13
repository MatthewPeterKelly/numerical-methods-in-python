#!/usr/bin/env python

from scipy.optimize import linprog

"""
Solve a basic linear programming problem using SciPy
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
"""

def main():
    """
    Minimize:  c^T * x
    Subject to:
        A_ub * x <= b_ub
        A_eq * x == b_eq
    """

    print('\n')
    print('**************************************************')
    print('Example from scipy.optimize.linprog documentation:')
    print('**************************************************')
    print('Minimize: [-1; 4] * x')
    print('Subject to:  [[-3, 1]; [1, 2]] * x < [6; 4]')
    c = [-1, 4]
    A = [[-3, 1], [1, 2]]
    b = [6, 4]
    x0_bounds = (None, None)
    x1_bounds = (-3, None)
    print('Solving...')
    result = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds),
                  options={"disp": True})
    print('Result:')
    print(result)

    print('\n')
    print('*********************************')
    print('Example from Math Stack Exchange:')
    print('http://math.stackexchange.com/questions/2011787/linear-programming-excercise')
    print('*********************************')
    print('Minimize: [1;2;3] * x')
    print('Subject to:')
    print(    '[[0,0,-3]; [-1, 1, 3]; [1,2,-3]] * x <= [-3; 4; -6]')
    print(    'x >= 0')
    c = [1, 2, 3]
    A = [[0,0,-3], [-1, 1, 3], [1,2,-3]]
    b = [-3, 4, 6]
    x0_bnd = (0, None)
    x1_bnd = (0, None)
    x2_bnd = (0, None)
    print('Solving...')
    result = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bnd, x1_bnd, x2_bnd),
                  options={"disp": True})
    print('Result:')
    print(result)

if __name__ == "__main__":
    main()
