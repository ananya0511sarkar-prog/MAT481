import sympy as sp
#import math as m #i don't need it for sqrt i can do it with sympy library


# define variable
x = sp.Symbol('x')

#the given function: 
f = (x**3)+(x**2)-1  #<--Give your function here
value1 = float(f.subs(x,0))
value2 = float(f.subs(x,1))
if(value1*value2>=0):
  print("It doesn't follow Intermediate Value Theorem. Hence it cannnot be solved using Fixed Point Iteration method.")
  exit()

# 4 transformation formulas
g1 =  1/(sp.sqrt(1+x))#(1 + x)**(-0.5)  #1/(m.sqrt(1+x)) i'm getting error 
g2 = (1 - x**3)**0.5
g3 = (1 - x**2)**(1/3)
g4 = -1/(sp.sqrt(1+x))#-(1 + x)**(-0.5)  #-1/(m.sqrt(1+x)) i'm getting error 

functions = [g1, g2, g3, g4]

#it's skipable
labels = [
    "1. x = (1 + x)^(-0.5)",
    "2. x = (1 - x^3)^0.5",
    "3. x = (1 - x^2)^(1/3)",
    "4. x = -(1 + x)^(-0.5)"
]

# Step 1: choose the first g(x) satisfying |g'(x)| <= 1 at x=0,0.5,0.1...
for i, g in enumerate(functions):
    g_prime = sp.diff(g, x)
    value = float(g_prime.subs(x, 0.1))#<--replace x=0,0.5,0.1...
    if abs(value) <= 1:
       chosen_g=g 
       print(f"Transformation chosen: Function {labels[i]}")
       break

# Step 2: Fixed Point Iteration
tol = 1e-6  #same as 10**(-6)
max_iter = 1000
x_old = 0.75  # initial guess which is in between (0,1)

for i in range(max_iter):
    x_new = float(chosen_g.subs(x, x_old))
    if abs(x_new - x_old) <= tol:
        print(f"Root found: x = {x_new:.6f} after {i+1} iterations")
        break
    x_old = x_new
else:
    print("Did not converge within the maximum number of iterations")
