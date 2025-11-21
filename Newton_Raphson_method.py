import sympy as sp

x = sp.Symbol('x')

def  Newton_Raphson(func, a,b, initial_guess, tol): #def  Newton_Raphson(func,initial_guess,tol):

        f= eval(func)
        value1 = sp.lambdify(x,f, "math") #we could've use value = f.subs(x,0)

        #check if it's following Intermediate Value Theorem
        if(value1(a)*value1(b)>=0):
                print(f"The given function {f} can't be solved by Newton-Raphson Method as it doesn't follow Intermediate Value Theorem.")
                #exit() #it stops the program and don't solve the next question so using return None is better option 
                return None

        diff_f = sp.diff(f,x)
        value2 = sp.lambdify(x,diff_f, "math")

        #check if the initial guess is within the interval
        if(initial_guess<a or initial_guess>b ):
              print(f"Initial guess isn't inside the interval for {f}")
              return None
        
        x_old = initial_guess
        max_iter=1000
        for i in range(max_iter):

            #check whether Newton-Raphson Method is suitable or not
            
            if  abs(value2(x_old)) < 1e-15: #here some fcorrection
                print("Derivative too small or step size , h is too large, might diverge. You better use Bisection Method.")
                break

            x_new = x_old -(value1(x_old)/value2(x_old))
            if abs(x_new-x_old)<=tol:
                   print(f"Root is found for {f} where x = {x_new:.6f} after {i+1} iteration")
                   break
            x_old = x_new
        else:
            print("Did not converge within the maximum iteration")
                   
Newton_Raphson("(3*(x**2))-(sp.exp(x))", 0 ,1, 0.75, 1e-6)   
Newton_Raphson("(3*(x**2))-(sp.exp(x))", 0 ,1, 2, 1e-6)#to check the initial guess is correct or not
Newton_Raphson("sp.sin(x)-0.5", 0 , sp.pi, 0.5, 1e-6 )#to check Intermediate value theorem
Newton_Raphson("sp.sin(x)-0.5", 0 , (sp.pi/2), 0.5, 1e-6 )
Newton_Raphson("x**3", -1 , 1 , 0 , 1e-6)
Newton_Raphson("x**3+(3*(x**2)-1)", -3, -2 , -2.5, 1e-6)
Newton_Raphson("sp.log(x-1)+sp.cos(x-1)", 1.3, 2,1.5,1e-6)#for sp.log(x) = ln(x)
#sp.log(x,10) = log(x) base 10,sp.log(x,2) = log(x) base 2
Newton_Raphson("(sp.cos(x))-(x*(sp.exp(x)))",0,1,0.75 ,1e-5)#assignment-1
Newton_Raphson("(x*(sp.log(x,10)))-12.34",1,20,10,1e-8)

