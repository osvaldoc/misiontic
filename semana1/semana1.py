# El # es un comentario, no se ejecuta, pero sirve como 
# documentacion
#La comilla doble hace cadena - string - str

#print("Una cadena es va comilla doble")

#Las variables se declaran INICIANDO con una letra
#no existe una variable que empiece con un numero
# 12245a= Malo, nombre=
# Preferiblemente las variables no deben tener caracteres de
# de español ñ,ó,í  no declarar con tildes
#Ejemplo: Variable a, a <- 50, numerica, entera, int
a = 50
#print(a)

#Variable b, numerica, decimal, float
b = 8.5
#print(b)

#Variable c, cadena, String, str
c = "Una cadena del curso de python y puedo poner ñ"
#print(c)

#Variable d, falso o verdadero, boolen, bool
d = True
#print(d)

e = False
#print(e)


#Variable f
f = 10 / (1 + 1)
#print(f)

f1 = 10 / (1 + 1 + 1)
#print(f1)

#Variable 
num1 = 9
num2 = 1
num3 = 8
suma = num1 + num2 + num3
#print (suma)

suma =  5 + num2
#print(suma)

resta = num3 - num1
#print(resta)

mult = num1 * num3
#print(mult)

#Yo no puedo "sumar"?? una cadena , con un numero
#Error: unsupported operand type(s) for +: 'int' and 'str'
#num4 = "juanita"
#suma = num1 + num4
#print(suma)

# al declarar tengo que asignar o sino sale error
# SyntaxError: invalid syntax
# div = 

# esto hizo div = 9 / 1
div = num1 / num2
#print(div)

# residuo de una division es el signo %, pilas con % 
# % con residuo
num1 = 10
num2 = 3
div = num1 / num2
#print(div)

res = num1 % num2
#print(res)

# // realiza la division y solo entrega la parte entera
# entero: es un numero pero no es decimal, sin puntos
cociente = num1 // num2
#print(cociente)

# orden jerarquico PEMDAS 
# Parentesis, Exponente, Multiplicación-División, Adición-Sustracción
resultado1 = 5 + 6 / 8 * 4
#print(resultado1)

resultado2 = (5 + 6) / (8 * 4)
#print(resultado2)

resultado2 = 5 + (6 / 8) * 4
#print(resultado2)

#Una practica no poner tildes en la declarion variables
año=2021
campaña = "unica"
#print(año)
#print(campaña)

#exponente es ** y ejemplo 2*2*2, 2 elevado 3, 2^3
numero_1 = 2
numero_2 = 3
exponente = numero_1 ** numero_2
#print(exponente)

numero_A = 3
numero_B = 3
exponente = numero_A ** numero_B # 3 elevado 3
#print(exponente)

#Variable c es de tipo falso, verdadero
#booleanas >, <, >=, <=, == (igual a), != (diferente a)
a = 3
b = 9
c = a > b
#print(c)

c = a < b
#print(c)

#OJO: una cosa es el igual y 
# otra distinta es el  igual-igual
# el igual asigna
# el igual-igual COMPARA
z = 3 # se lee asi: z asignele 3
a == z # se lee asi: a es igual  z? 
c = (a == z)
#print(c)

c = (a == b) # 3 es igual 9
#print(c)

c = (a != b) # 3 es diferente 9
#print(c)

c=True
#print(c)

p1 = (5==5) # Verdadero, True
p2 = (5 != 5) # Falso, False
#print(p2)

# V and V = True
respuesta = p1 and p1
#print(respuesta)

# V and F = False
respuesta = p1 and p2
#print(respuesta)

# F and V  = False
respuesta = p2 and p1
#print(respuesta)

# F and F = False
respuesta = p2 and p2
#print(respuesta)

#Tabla de verdad de and
#print(True and True)
#print(True and False)
#print(False and True)
#print(False and False)


#Tabla de verdad de or
#print(True or True)
#print(True or False)
#print(False or True)
#print(False or False)

