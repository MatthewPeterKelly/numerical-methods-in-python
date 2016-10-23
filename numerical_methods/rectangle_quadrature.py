from .quadrature_method import QuadratureMethod


class RectangleQuadrature(QuadratureMethod):
    """
    Perform numerical integration (quadrature) using the rectangle rule
    """

    def evaluate(self):
        h = self._upp - self._low
        f = self._fun(0.5*self._upp + 0.5*self._low)
        return h*f
