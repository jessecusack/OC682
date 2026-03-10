# Resources

This page collates various useful resources, many of which were drawn upon during recent development of OC682. 

## Classes

Other great data analysis classes with public material exist, including:

[SIOC221a](https://pordlabs.ucsd.edu/sgille/sioc221a/), [SIOC221b](https://pordlabs.ucsd.edu/sgille/sioc221b/) and [SIO221c](https://pordlabs.ucsd.edu/sgille/sio221c/): A trio of data analysis courses at Scripps for oceanographers. 

[Phy 411](https://jklymak.github.io/Phy411/): A time series analysis class taught at the University of Victoria.

[Ocean / Atmosphere Time Series Analysis](https://jmlilly.net/course/): Jonathan Lilly's class.

## Books

[Python for Data Analysis](https://wesmckinney.com/book/): An excellent resource from the creator of Pandas. 

[An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro.html): An online book for the class of the same name developed at Columbia University.  

## Python Packages

[NumPy](https://numpy.org/) and [SciPy](https://scipy.org/) provide the foundation for much of the scientific python ecosystem. The NumPy homepage gives a great overview of the ecosystem's most useful packages (as of Feb 2026) and we do not need to repeat it here. Less broadly used packages include: 

[xarray](https://docs.xarray.dev/en/stable/): Labelled N-dimensional arrays with lots of smart methods. Works well with data in netCDF format. 

[statsmodels](https://www.statsmodels.org/stable/index.html): A huge library of statistical models. Useful for estimating properly scaled autocorrelation among many other things. 

[odrpack](https://hugomvale.github.io/odrpack-python/): Orthogonal distance regression. Good for fitting an ellipse, and for regression with errors in both dependent and independent variables. 

[awkward](https://awkward-array.org/doc/main/): For when your data does not fit into regular grids. Methods otimized for ragged arrays. 