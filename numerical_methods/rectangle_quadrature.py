from .quadrature_method import QuadratureMethod
import numpy as np


class RectangleQuadrature(QuadratureMethod):
    """
    Perform numerical integration (quadrature) using the rectangle rule
    """

    def evaluate(self):
        """
        Rectangle quadrature works by approximating each segment of the
        integrand as a constand value. In pseudo code:
        J = sum(h*f)
        where J is the approximation of the integral, h is the duration of
        each segment and f is the value of the integrand
        There are three common types of rectangle quadrature, based on the
        location of the quadrature point: lower, middle, upper.
        In general, selecting the middle point in the segment will yield the
        best results.
        """
        if self._knots is None:
            self.create_uniform_segments(50)

        # Use the middle of the segment for now
        t_knot = self._knots
        N = len(t_knot)
        t_low = t_knot[0:N-1]
        t_upp = t_knot[1:N]
        t = 0.5*(t_low+t_upp)   # quadrature points  (middle of each segment)

        # rectangle quadrature!
        h = t_upp - t_low  # segment duration
        f = self._fun(t)  # value of the function at quadrature points
        J = np.sum(h*f)  # add up all of the little rectangles

        return J
