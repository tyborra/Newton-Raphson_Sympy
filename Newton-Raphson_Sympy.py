
def newton_raph(fx, theta_0, thresh, x_data):        
    ''''    Function to implement the Newton Raphson method
    '''
        
    #get the first and second derivative
    d1 = sp.diff(fx, theta)
    d2 = sp.diff(d1, theta) 
   
    print('\nLatex Equations')
    print('Original Function:  ', sp.latex(fx))
    print('First Derivative:   ', sp.latex(d1))
    print('Second Derivative:  ',sp.latex(d2))
    
    #initialize the first derivative
    d_sub = d1.subs(theta, theta_0)    
    d1_lam = sp.lambdify( x, d_sub, "numpy")
    d_1 = sum((d1_lam(x_data)))
    
    #Iterate using the Newton Raphson method while theta is < thresh
    n_iterations = 0    #Number of iterations to complete
    
    while abs(d_1) > thresh: 
        n_iterations +=1
        d1_sub = d1.subs(theta, theta_0)
        d1_lam = sp.lambdify( x, d1_sub, "numpy")
        d_1 = np.sum((d1_lam(x_data)))
        
        d2_sub = d2.subs(theta, theta_0)
        d2_lam = sp.lambdify( x, d2_sub, "numpy")
        d_2 = np.sum((d2_lam(x_data)))        
        
        #assign new value to theta for next iteration         
        theta_0 = theta_0 - d_1/d_2         
        
    theta_hat = theta_0
    print('\nNumber of Iterations: ', n_iterations)
    print('theta hat: ', theta_hat)    
    return theta_hat   


if __name__ == "__main__":
    import sympy as sp
    from sympy.abc import i
    import numpy as np 
    import pandas as pd    
    
    #Sample 1    
    #create synthetic data
    n=10
    j=np.arange(1,n+1,1)
    x_data = -3.1 + 6*j/n
    
    #declare the sympy function
    theta = sp.Symbol('theta')
    x = sp.Symbol('x')
    
    fx = 1551*theta - sp.Sum( (sp.exp(theta*x) ),(i, 0, 9))
    theta_init = 3    #initial guess of theta
    thresh = 1e-10    #threshold for theta
    
    #Sample 2 (work in progress)
# =============================================================================
#     data = pd.read_csv(r'data/test_data.csv')
#     x_data = data['x']
#     y_data = data['y']  
#     
#     theta = sp.Symbol('theta')
#     x = sp.Symbol('x')
#     y = sp.symbol('y')
#     
#     fx = 1/2 * sp.sum( (y-sp.exp(theta*x))**2),(i, 0, len(x_data-1)))
# =============================================================================
    
    
    #run function
    newton_raph(fx=fx, theta_0=theta_init, thresh=thresh, x_data = x_data)
    