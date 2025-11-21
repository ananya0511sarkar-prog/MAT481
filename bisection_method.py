import math #for e^x , cos(x)
def bisection_method(func, a, b,tol):
     
     def f(x):
          f=eval(func)
          return f
     
     error = abs(b-a)
     while error > tol:
              c = (a+b)/2
     
              if f(a)*f(b)>=0:
                   print("Same sign hence not aplicable")
                   
              elif f(c)*f(b)<0:
                   a=c
                   error = abs(b-a)
              elif f(c)*f(a)<0:
                   b=c
                   error = abs(b-a)
              else:
                   print("Something is wrong")
                   quit()
     print(f"The error is {error} and the lower boundary is {a} and upper boundary is {b}")
     print(f"The final answer is {b:.6f}")  

#for every problem tollerance is 10^-3 = 0.001
print("CW: x^3-x-1=0; (1,2)")
bisection_method("(x**3)-x-1",1,2,0.001)
print("HW: x^3+4x^2-10=0; (1,2)")
bisection_method("(x**3)+(4*(x**2))-10",1,2,0.001)
print("HW: e^x-x^2+3x-2=0; (0,2)")
bisection_method("(math.exp(x))-(x**2)+(3*x)-2",0,2,0.001)
print("HW: 2^x+3cosx-e^x=0;(1,2)")
bisection_method("(2*x)+(3*(math.cos(x)))-(math.exp(x))",1,2,0.001)
print("2x-cos(x)-3; (0,pi)")
bisection_method("(2*x)-math.cos(x)-3", 0, math.pi, 0.001)
bisection_method("(x**(0.5))-math.cos(x)",0,1,0.01)
bisection_method("(2*x*math.cos(2*x))-(x+1)**2", -1,0,1e-5)
bisection_method("(x**4)+(3*(x**2))-2",0,1,1e-5)
bisection_method("(8*x**3)-(12*x**2)-(2*x)+5",1,2,1e-3)#assignment-1 problem
bisection_method("math.cos(x)-(x*(math.exp(x)))",0,1,1e-5)
     