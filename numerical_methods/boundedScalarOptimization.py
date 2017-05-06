#! /usr/bin/env python

import math

def test_function(x):
    """
    A scalar test function with a single minimum value on [-1,1]
    """
    x_zero = 0.1234
    return (x - x_zero)*(x - x_zero)


def bounded_scalar_optimization(fun, x_low, x_upp, tol=1e-8, max_fun_eval=50):
    """
    Compute the minimum value of a scalar function on the domain [x_low, x_upp]
    @param fun: a scalar function
    @param x_low: lower bound for the search
    @param x_upp: upper bound for the search
    """

    # Use a simple bisection search to bracket the minimum:
    xa = x_low
    xc = x_upp
    fa = fun(xa)
    fc = fun(xc)
    flag_is_bracketed = False
    eval_count = 2
    while abs(xa-xc) > tol and eval_count < max_fun_eval:
        xb = 0.5*(xa + xc)
        fb = fun(xb)
        eval_count += 1
        if fb < fa and fb < fc:  # success! root is bracketed
            flag_is_bracketed = True
            break
        if fa < fc:  # contract towards xa
            xc = xb
            fc = fb
        else:  # contract towards xc
            xa = xb
            fa = fb

    # Check if the bisection search worked:
    if not flag_is_bracketed:
        if fa < fc:
            x_best = xa
            f_best = fa
            exit_code = 1
            exit_msg = 'minimum at lower bound'
        else:
            x_best = xc
            f_best = fc
            exit_code = 2
            exit_msg = 'minimum at upper bound'

    else:  # bisection worked!  perform golden section search

        # Initialization
        R = 2 / (1 + 5 ** 0.5)  # inverse golden ratio
        C = 1 - R  # Useful constant

        x0 = xa
        x3 = xc
        if abs(xc - xb) > abs(xb - xa):
            x1 = xb
            x2 = xb + C*(xc - xb)
        else:
            x1 = xb - C*(xb - xa)
            x2 = xb

        # Evaluate mid-points:
        f1 = fun(x1)
        f2 = fun(x2)

        # Optimization loop:
        iter_count = 0
        converged = True
        while abs(x3-x0) > tol:
            if f2 < f1:
                x0 = x1
                x1 = x2
                x2 = R*x1 + C*x3
                f1 = f2
                f2 = fun(x2)
                eval_count += 1
            else:
                x3 = x2
                x2 = x1
                x1 = R*x2 + C*x0
                f2 = f1
                f1 = fun(x1)
                eval_count += 1
            # Update the best solution:
            if f1 < f2:
                x_best = x1
                f_best = f1
            else:
                x_best = x2
                f_best = f2
            # Check number of function iterations
            if eval_count >= max_fun_eval:
                exit_code = 3
                exit_msg = 'reached maximum iterations at interior point'
                converged = False
                break

        if converged:
            exit_code = 0
            exit_msg = 'converged to minimum at interior point'

    # Return the solution as a dictionary
    soln = dict()
    soln['x'] = x_best
    soln['f'] = f_best
    soln['eval_count'] = eval_count
    soln['exit_code'] = exit_code
    soln['exit_msg'] = exit_msg
    return soln


if __name__ == '__main__':
    fun = test_function
    x_low = -1.0
    x_upp = 1.0
    soln = bounded_scalar_optimization(fun, x_low, x_upp)
    print(soln)
