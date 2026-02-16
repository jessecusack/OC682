# Mathematical Foundations

We begin with some useful definitions that we will use throughout the course. We are beginning to build the tools for statistical data analysis.

## Ordered Process

A process that is ordered by one or more independent variables.

$y(t)$ is an example of a univariate ordered process (one _dependent_ variable). In our class, time, $t$, will almost always be our independent variable (though we will sometimes use more than one independent variable (e.g., space, $\vec{x}$, or space and time, $\vec{x},t$).

We might have more than one dependent variable (multivariate process), $\vec{y}(t)$, which could represent, for example, currents, temperature, salinity, dissolved oxygen \... ($u(t)$, $v(t)$, $w(t)$, $T(t)$, $S(t)$, $O_{2}(t)$, \...).

## Deterministic Ordered Process

A process whose dependence on the independent variable can be described by an explicit mathematical relationship. That is, a process that is completely determined by its initial state. For example:

$$y(t) = A\cos(2\pi ft + \phi)$$

In the ocean, tides are nearly a deterministic process.

## Stochastic (random) Process

A process that has some degree of unpredictability. At any time, $t = t_\mathrm{o}$, $y$ is governed by a probability law that is characterized by a probability distribution function (pdf).

The probability law may not be the same for all times. This distinguishes a stationary process from a non-stationary process.

<!-- <figure id="fig1">
<div class="center">
<img src="Lecture1Figure1.jpg" style="width:5in" />
</div>
<figcaption>An example of a probability function, <span
class="math inline"><em>p</em><sub><em>Y</em></sub>(<em>y</em>)</span>.</figcaption>
</figure> -->

## Complex Numbers

Even though the (physical, biological, economic, \...) processes we consider in data analysis are real, it is often mathematically convenient to express them as complex numbers. For example, this can make derivations and analyses easier and less cumbersome.

$$y(t) \equiv y_{R}(t) + iy_{I}(t)$$

$$i = \sqrt{-1} \; \mathrm{,} \;\;\; i^2 = -1 \; \mathrm{,} \;\;\;  \frac{1}{i} = \frac{1}{i}\frac{i}{i} = -i$$

The complex conjugate of $y(t)$ is:

$$y^{*}(t) = y_{R}(t) - iy_{I}(t)$$

The inner product of a complex number is:

$$y^{*}y = yy^{*} = (y_{R} - iy_{I})(y_{R} + iy_{I}) = y_{R}^2 + y_{I}^2$$

## Euler's number, $e$, and Euler representation of a complex number

$$\ln(e) = 1$$

$$e \equiv \lim_{n \to \infty} (1 + \frac{1}{n})^n = \sum^{\infty}_{m=0}\frac{1}{m!}= 2.718281828...$$

$$e^{-1}  = \lim_{n \to \infty} (1 - \frac{1}{n})^n$$

The Taylor expansion of $e^x$ is given by:

$$e^{x} = 1 + x + \frac{1}{2!}x^2 + \frac{1}{3!}x^3 + ...$$

We can use this Taylor expansion (and the Taylor expansions for $\cos$
and $\sin$) to show that:

$$e^{i\phi} = \cos(\phi) + i \sin(\phi)$$

so that, in Euler form, a complex number can be expressed as:

$$y(t) = y_R(t) + i y_I(t) = A(t)e^{i\phi(t)} = A(t)\cos(\phi(t)) + iA(t)\sin(\phi(t))$$

where $A$ and $\phi$ are real numbers.

$$y^* = Ae^{-i\phi}$$

$$y^*y = A^2$$

Notice that the inner product is independent of phase, $\phi$.

$$1 = e^0 \:,\; i = e^{i\frac{1}{2}\pi} \:,\; -1 = e^{i\pi} \:,\; -i = e^{i\frac{3}{2}\pi}$$

$$\cos{\phi} = \frac{1}{2}(e^{i\phi} + e^{-i\phi})$$

$$\sin{\phi} = \frac{1}{2i}(e^{i\phi} - e^{-i\phi})$$

## Even and odd functions.

Any function can be expressed as the sum of an even and an odd part.

*Even (symmetric) function*: $y(-t) = y(t)$

*Odd (anti-symmetric) function*: $y(-t) = - y(t)$

<!-- <figure id="fig2">
<div class="center">
<img src="Lecture1Figure2.jpg" style="width:5in" />
</div>
<figcaption>Artistic renditions of examples of even (left) and odd
(right) functions.</figcaption>
</figure> -->

$$y(t) = \frac{1}{2} [ y(t) + y(-t) ] +  \frac{1}{2} [ y(t) - y(-t) ]$$

The first expression on the right is an even function, while the second expression on the right is an odd function.

When an even function is multiplied by an even function, the resulting function is an even function (E$\times$E = E). What about:

O$\times$O = ?

O$\times$E = ?

E$+$E = ?

O$+$O = ?

E$+$O = ?

## Hermitian Function

$$y(t) = y^*(-t)$$

The real part of a Hermitian function is even, while the imaginary part is odd.

## Periodic process.

$$y(t) = y(t + kT)$$

where $k$ is an integer and $T$ is the *period* of the process.

## Monochromatic sinusoidal process

$f$ = frequency \[cycles per unit time\]

$\omega$ = $2\pi f$ = angular frequency \[radians per unit time\]

$T= \frac{2\pi}{\omega} = \frac{1}{f}$ = period

$$y(t) = A\cos(2\pi f t + \phi) = A \, \mathrm{Re} [e^{i(2\pi f t + \phi)}]$$

In the above expression, $A$ and $\phi$ are real. By $\mathrm{Re}$, we mean take only the real part of the expression. We can also express $y(t)$ as:

$$y(t) = \mathrm{Re} [A'e^{i2\pi f t }] \, , \; A' = Ae^{i\phi}$$

Where $A'$ is complex and contains phase information. As mentioned above, these complex functions are convenient for derivations and/or analyses. In which case, we ignore the $\mathrm{Re}$ while doing the derivation or analyses, but remember to take only the real part at the end.

------------------------------------------------------------------------

------------------------------------------------------------------------

*Aside:*

\begin{align}
y(t) & =  A\cos(2\pi f t + \phi) \nonumber \\
      & =  A\cos(\phi)\cos(2\pi f t) - A\sin(\phi)\sin(2\pi f t) \nonumber \\
      & \equiv a_{\mathrm{cos}}\cos(2\pi f t) + a_{\mathrm{sin}}\sin(2\pi f t) 
 
\end{align}

$$A = [a_{\mathrm{cos}}^2 + a_{\mathrm{sin}}^2]^{1/2}$$

$$\phi = \tan^{-1}(-\frac{a_{\mathrm{sin}}}{a_{\mathrm{cos}}})$$

------------------------------------------------------------------------

------------------------------------------------------------------------

Taking derivatives in Euler form can be much easier to keep track of compared to taking derivatives of sines and cosines. For example:

$$\frac{d}{dt}A'e^{i2\pi f t} = (i2\pi f )A'e^{i2\pi f t}$$

$$\frac{d^n}{dt^n}A'e^{i2\pi f t} = (i2\pi f )^nA'e^{i2\pi f t}$$
