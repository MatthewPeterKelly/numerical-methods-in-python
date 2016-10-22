from abc import ABCMeta, abstractmethod

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

    @abstractmethod
    def evaluate(self): pass
