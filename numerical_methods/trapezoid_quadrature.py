from .quadrature_method import QuadratureMethod
import numpy as np


class TrapezoidQuadrature(QuadratureMethod):
    """
    Perform numerical integration (quadrature) using the trapezoid rule
    """

    def evaluate(self):
        """
        Trapezoid quadrature works by approximating each segment of the
        integrand as a linear function. The area under a linear function looks
        like a trapezoid and we can use basic geometry to evaluate the area.
        In pseudo code:        J = sum( 0.5*h*(fLow + fUpp) )
        where J is the approximation of the integral, h is the duration of
        each segment, fLow is the value at the lower edge of the interval, and
        fUpp is the function value at the upper edge of the interval.
        """
        if self._knots is None:
            self.create_uniform_segments(50)

        t_knot = self._knots  # quadrature points
        N = len(t_knot)
        t_low = t_knot[0:N-1]
        t_upp = t_knot[1:N]
        h = t_upp - t_low
        f_knot = self._fun(t_knot)  # function value at each knot point
        f_low = f_knot[0:N-1]
        f_upp = f_knot[1:N]
        J = np.sum(0.5*h*(f_low + f_upp))  # add up the trapezoids

        return J
