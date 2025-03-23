import sympy as sym # importar librerias
#Declarar variable
x= sym.Symbol('x')
func = input('Ingrese la funcion: \n')#Pedir fumcion
result =sym.Derivative(func,x,evaluate =True)#Derivar la funcion
print(result)# Mostrar resultado
