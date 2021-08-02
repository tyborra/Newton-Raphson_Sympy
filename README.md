# Newton-Raphson Method with Sympy
The Newton-Raphson method uses an iterative method to find roots of equations. The method begins with an initial guess of the optimal value, then uses the following process until theta is less than a predefined threshold.

$\\\Large \theta _{(t+1)} =  \theta_{t}-\frac{f'(\theta_{t})}{f''(\theta_{t})}\\$ 

This implmentation uses Sympy to compute the first and second derivative before using them to find the root. No calculus is required.

