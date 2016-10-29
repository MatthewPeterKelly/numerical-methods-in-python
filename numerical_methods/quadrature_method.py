from abc import ABCMeta, abstractmethod
import numpy as np


class QuadratureMethod(object):
    """
    An abstract super-class for all quadrature methods
    """

    def __init__(self, function_handle, lower_bound, upper_bound):
        """
        Creates a quadrature method object.
        @param function_handle: a scalar function to be integrated.
        @param low: lower integration bound
        @param upp: upper integration bound
        """
        self._fun = function_handle
        self._low = lower_bound
        self._upp = upper_bound
        self._knots = None  # Default value, let methods define

    def create_uniform_segments(self, segment_count):
        """
        In quadrature, the function is broken up into segments, where each
        segment stretches between two knot points. Quadrature works by
        approximating each the function on segment as a continuous polynomial.
        The approximation (or its derivative) can be discontinuous at the
        knot points. Look up 'piecewise polynomial' or 'polynomial spline' for
        more details.
        @param segment_count: number of uniform segments to create.
        """
        self._knots = np.linspace(self._low, self._upp, segment_count + 1)

    @abstractmethod
    def evaluate(self): pass
