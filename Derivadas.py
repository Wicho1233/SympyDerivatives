import sympy as sym # importar librerias
#Declarar variable
x= sym.Symbol('x')
#Pedir fumcion
func = input('Ingrese la funcion: \n')
result =sym.Derivative(func,x,evaluate =True)#Derivar la funcion
print(result)# Mostrar resultado
