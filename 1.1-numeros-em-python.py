# ==========================================
# AULA COMPLETA : NÚMEROS EM PYTHON
# ==========================================

"""
VAMOS APRENDER:
1 - Tipos numéricos
2 - Conversões de tipos
3 - Operações matemáticas
4 - Verificação de tipos
"""

# ==========================================
# PASSO 01 - TIPOS NUMÉRICOS
# ==========================================

print("===== TIPOS NUMÉRICOS =====")

# EXEMPLO 01 - NÚMERO INTEIRO
numero_inteiro = 10

print("Valor:", numero_inteiro)
print("Tipo:", type(numero_inteiro))

print("-------------------")

# EXEMPLO 02 - NÚMERO DECIMAL
numero_decimal = 3.14

print("Valor:", numero_decimal)
print("Tipo:", type(numero_decimal))

print("-------------------")

# EXEMPLO 03 - NÚMERO COMPLEXO
numero_complexo = 2 + 3j

print("Valor:", numero_complexo)
print("Tipo:", type(numero_complexo))

print("Parte real:", numero_complexo.real)
print("Parte imaginária:", numero_complexo.imag)

print("\n")


# ==========================================
# PASSO 02 - CONVERSÃO DE TIPOS
# ==========================================

print("===== CONVERSÕES =====")

# float para int
valor = int(3.9)

print("int(3.9):", valor)
print("Tipo:", type(valor))

print("-------------------")

# string para int
valor1 = "10"

print("Antes:", type(valor1))

valor2 = int(valor1)

print("Depois:", valor2)
print("Tipo:", type(valor2))

print("-------------------")

# int para float
valor3 = float(10)

print("float(10):", valor3)
print("Tipo:", type(valor3))

print("\n")


# ==========================================
# PASSO 03 - OPERAÇÕES MATEMÁTICAS
# ==========================================

print("===== OPERAÇÕES =====")

a = 10
b = 5

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)

print("\n")


# ==========================================
# PASSO 04 - STRINGS EM PYTHON
# ==========================================

print("===== STRINGS =====")

texto1 = "Python"
texto2 = 'Curso de Python'

print(texto1)
print(texto2)

print("-------------------")

# Aspas dentro da string
texto3 = "copa 'padrão fifa'"
texto4 = 'copa "padrão fifa"'

print(texto3)
print(texto4)

print("-------------------")

# String multilinha
menu = """
-H Exibe ajuda
-U Url do sistema
"""

print(menu)

print("-------------------")

# Concatenação automática
texto = ("Python" " é " "muito legal")

print(texto)

print("-------------------")

# Strings como sequência
st = "maracana"

print("Primeira letra:", st[0])
print("Última letra:", st[-1])
print("Trecho 1:4:", st[1:4])
print("Do início até 3:", st[:3])
print("Do 2 até o fim:", st[2:])
print("Tamanho:", len(st))