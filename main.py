import numpy as np
import buildPlot as plot
import Lagrange as L
import Newton as N
import smoothingPolynom as sm

# данные 1 варианта
Xn = np.array([1, 2, 3, 4, 5])
Fxn = np.array([4., 2., 8., 1., -1.])

plot.build(Xn, Fxn)
plot.buildInterpolated(L.Lagrange, Xn, Fxn)
plot.buildInterpolated(N.Newton, Xn, Fxn)

# пример из теории.
# Xn = np.array([1, 2, 3, 4, 5])
# Fxn = np.array([1, 3, 1, 4, 2])
plot.buildSmooth(sm.calculate, Xn, Fxn, 1)
plot.buildSmooth(sm.calculate, Xn, Fxn, 2)
plot.buildSmooth(sm.calculate, Xn, Fxn, 3)
