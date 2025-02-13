import sympy as sym
x= sym.Symbol('x')
func = input('Ingrese la funcion: \n')
result =sym.Derivative(func,x,evaluate =True)
print(result)