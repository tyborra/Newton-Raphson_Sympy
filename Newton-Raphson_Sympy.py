
def newton_raph(fx, theta_0, thresh, x_data):        
    n_iterations = 0
    
    #get d1 and d2
    d1 = sp.diff(fx, theta)
    d2 = sp.diff(d1, theta) 
    
    #initialize theta1
    d_sub = d1.subs(theta, theta_0)
    d1_lam = sp.lambdify( x, d_sub, "numpy")
    d_1 = sum((d1_lam(x_data)))
    
    while abs(d_1) > thresh: 
        n_iterations +=1
        d1_sub = d1.subs(theta, theta_0)
        d1_lam = sp.lambdify( x, d1_sub, "numpy")
        d_1 = np.sum((d1_lam(x_data)))
        
        d2_sub = d2.subs(theta, theta_0)
        d2_lam = sp.lambdify( x, d2_sub, "numpy")
        d_2 = np.sum((d2_lam(x_data)))        
        
        print('\niter: ',n_iterations)
        print('theta: ', theta_0)
        print('d1: ', d_1)
        
        theta_0 = theta_0 - d_1/d_2         
        
    theta_hat = theta_0
    print('theta hat: ', theta_hat)    
    return theta_0    


if __name__ == "__main__":
    import sympy as sp
    from sympy.abc import i
    import numpy as np
    
    #create data
    n=10
    j=np.arange(1,n+1,1)
    x_data = -3+6*j/n

    #declare the sympy function
    theta = sp.Symbol('theta')
    x = sp.Symbol('x')
    fx = 1551*theta -sp.Sum( (sp.exp(theta*x) ),(i, 0, 9))


    #run function
    newton_raph(fx=fx, theta_0=3, thresh=1e-10, x_data = x_data)