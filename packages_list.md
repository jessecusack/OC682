# Useful Python Packages

## The foundational packages

[NumPy](https://numpy.org/) and [SciPy](https://scipy.org/) provide the foundation for so much of the scientific python ecosystem. The NumPy homepage gives a great overview of the ecosystem's most useful packages (as of Feb 2026) and we do not need to repeat it here. 

## Beyond the foundations

[xarray](https://docs.xarray.dev/en/stable/): labelled N-dimensional arrays with lots of smart methods. Works well with data in netCDF format. 

[statsmodels](https://www.statsmodels.org/stable/index.html): A huge library of statistical models. Useful for estimating properly scaled autocorrelation among many other things. 

[odrpack](https://hugomvale.github.io/odrpack-python/): Orthogonal distance regression.Good for fitting an ellipse, and for regression with errors in both dependent and independent variables. 

[awkward](https://awkward-array.org/doc/main/): For when your data does not fit into regular grids. Methods ptimized for ragged arrays. 