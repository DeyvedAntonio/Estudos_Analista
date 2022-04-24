# Sintaxe básica
print('Hello world!')

# Variáveis
a = 30
b = 46

# Operadores matemáticos
soma = a + b
subtracao = b - a
divisao = b / a
multiplicacao = a * b
exponenciacao = a ** b
modulo = a % b
divisao_chao = b // a

# tipos de dados
lista = []
tupla = ()
dicionario = {}

# comando Built-in
print(round(divisao, 3))
print(len(str(multiplicacao)))

# fatiamento
string = 'Como usar fatiamento no Python'
print(string[0:5])
print(string[0:-1])
print(string[-12:-2])
print(string[0:])

# manipulação de strings
manipulacao1 = string.replace('fatiamento', 'manipulação')
manipulacao2 = string.startswith('Python')
manipulacao3 = string.endswith('Python')
manipulacao4 = string.count(manipulacao1)
manipulacao5 = string.capitalize()
manipulacao6 = string.isdigit()
manipulacao7 = string.isalnum()
manipulacao8 = string.upper()
manipulacao9 = string.lower()
manipulacao10 = string.find('o')


print(manipulacao1, manipulacao2, manipulacao3, manipulacao4, manipulacao5, manipulacao6)
print(manipulacao7, manipulacao8, manipulacao9, manipulacao10)

# Operadores de comparação
operador1 = 1
operador2 = 2
operador3 = 3
operador4 = 2

print('==', operador1 == operador4)
print('==', operador2 == operador4)
print('!=', operador3 != operador1)
print('!=', operador2 != operador4)
print('>', operador2 > operador1)
print('>', operador3 > operador4)
print('<', operador2 < operador4)
print('>=', operador1 >= operador3)
print('<=', operador1 <= operador2)

# operadores lógicos

opera1 = True
opera2 = False

print('and', opera1 and opera2)
print('and', opera1 and opera1)
print('or', opera1 or opera2)
print('or', opera2 or opera2)
print('not', not opera2)
print('not', not opera1)

# operadores de associação

lista = ('Abacate', 1, 3, 5.5)
print("como" in string)
print('operador1' in string)
print(operador1 not in lista)
print(operador2 not in lista)

# operadores identidade

string2 = 'Teste de comportamento'

print(string is string2)
print(string is string)

# pacote datetime

import datetime

dia_hoje = datetime.datetime.today()
print(dia_hoje)

data = datetime.datetime.today()
print(data.strftime('%d/%m/%y'))

# pacote time

import time

print(1)
time.sleep(0.01)
print(5)
print(time.time())

# pacote math

import math

tupla = (10, 5, 20, 30, 40)
print(min(tupla))
print(max(tupla))
print(abs(-7.25))
print(pow(3, 4))
print(pow(tupla[2], 2))
print(math.sqrt(81))
print(math.ceil(1.6))
print(math.floor(1.4))
print(math.pi)

# pacote random

import random

lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.choice(lista))
print(random.random())
print(random.randint(1, 10))

# pacote statistics

import statistics

lista = [12, 15, 28, 56, 78, 80]
print(sum(lista)/len(lista))
print(statistics.mean(lista))
print(statistics.median(lista))
print(statistics.mode(lista))

# condicional IF

if opera1 == True:
    print('Verdade')
else:
    print('Falso')

if opera1 == opera2:
    print('Operadores com valores lógicos iguais')
else:
    print('Operadores com valores lógicos diferentes')

if opera1 and opera2:
    print(True)
elif (opera1 and opera2) or opera2:
    print(True)
else:
    print(False)

# laço for

for i in lista:
    print(i)

lista_pais = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai', 'Bolivia', 'Chile']

for pais in lista_pais:
    print(pais)
    print(pais.upper())
    print(pais.upper()[0:3])
    if pais == 'Uruguai':
        print('É bicampeão mundial')

for loop in range(len(lista_pais)):
    print(lista_pais[loop])

