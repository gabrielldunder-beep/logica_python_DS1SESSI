# EX1
# Um aluno tem 10 anos. Armazene essa idade em uma variável
# e exiba seu tipo.

idade = 10

print("Idade:", idade)
print("Tipo:", type(idade))


# EX2
# A temperatura medida é 23.5°C.
# Armazene esse valor e mostre seu tipo.

temperatura = 23.5

print("Temperatura:", temperatura)
print("Tipo:", type(temperatura))


# EX3
# Crie um número complexo representando uma impedância elétrica
# de 5 + 8j e mostre sua parte real.

impedancia = 5 + 8j

print("Parte real:", impedancia.real)


# EX4
# Mostre a parte imaginária do número complexo
# criado no exercício anterior.

print("Parte imaginária:", impedancia.imag)


# EX5
# Declare uma variável chamada "populacao"
# com o valor 8_000_000_000 (8 bilhões)
# e mostre seu tipo.

populacao = 8_000_000_000

print("População:", populacao)
print("Tipo:", type(populacao))


# EX6
# Verifique se o número 7 é do tipo int
# usando a função type().

print("7 é int?", type(7) == int)


# EX7
# Crie uma variável chamada "aprovado"
# com o valor booleano True e mostre seu tipo.

aprovado = True

print("Aprovado:", aprovado)
print("Tipo:", type(aprovado))


# EX8
# Some True e False e mostre o resultado
# e também o tipo do resultado.

resultado = True + False

print("Resultado:", resultado)
print("Tipo:", type(resultado))


# EX9
# Pesquise e mostre qual é o valor máximo
# que um número inteiro pode ter em Python.

import sys

print("Valor máximo:", sys.maxsize)


# EX10
# Mostre a representação em binário
# do número 10 usando uma função do Python.

print("Binário de 10:", bin(10))