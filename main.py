import numpy as np
import buildPlot as plot
import Lagrange as L
import Newton as N

Xn = np.array([1, 2, 3, 4, 5])
Fxn = np.array([4., 2., 8., 1., -1.])

#plot.build(Xn,Fxn)
plot.buildInterpolated(L.Lagrange,Xn,Fxn)
plot.buildInterpolated(N.Newton,Xn,Fxn)


