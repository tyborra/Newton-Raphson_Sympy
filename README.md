# Newton-Raphson Method with Sympy
The Newton-Raphson method uses an iterative method to find roots of equations. The method begins with an initial guess of the optimal value, then uses the following process until theta is less than a predefined threshold.

<img src="https://render.githubusercontent.com/render/math?math=\\\Large\theta_{(t%2B1)}=\theta_{t}-\frac{f'(\theta_{t})}{f''(\theta_{t})}\\">


This implementation uses Sympy to compute the first and second derivative before using them to find the root. 

