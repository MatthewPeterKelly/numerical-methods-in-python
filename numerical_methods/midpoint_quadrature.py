from .quadrature_method import QuadratureMethod
import numpy as np


class MidpointQuadrature(QuadratureMethod):
    """
    Perform numerical integration (quadrature) using the Midpoint rule
    """

    def evaluate(self):
        """
        Midpoint quadrature works by approximating each segment of the
        integrand as constant, using the value at the segment midpoint.
        In pseudo code:  J = sum(h*f)
        where J is the approximation of the integral, h is the duration of
        each segment and f is the value of the integrand.
        """
        if self._knots is None:
            self.create_uniform_segments(50)

        # Compute the midpoint of each segment
        t_knot = self._knots
        N = len(t_knot)
        t_low = t_knot[0:N-1]
        t_upp = t_knot[1:N]
        t = 0.5*(t_low+t_upp)   # quadrature points  (middle of each segment)

        # Midpoint quadrature!
        h = t_upp - t_low  # segment duration
        f = self._fun(t)  # value of the function at segment midpoints
        J = np.sum(h*f)  # add up all of the little rectangles

        return J
