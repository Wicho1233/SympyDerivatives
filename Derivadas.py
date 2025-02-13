import sympy as sym # importar librerias
x= sym.Symbol('x')#Declarar variable
func = input('Ingrese la funcion: \n')#Pedir fumcion
result =sym.Derivative(func,x,evaluate =True)#Derivar la funcion
print(result)# Mostrar resultado