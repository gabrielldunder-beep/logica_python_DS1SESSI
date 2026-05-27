# ==========================================
# AULA COMPLETA: NÚMEROS EM PYTHON
# ==========================================

"""
VAMOS APRENDER:
1 - Tipos Numéricos
2 - Conversões de Tipos
3 - Hierarquia Numérica
4 - Operações Matemáticas
5 - Coerção de Tipos
6 - Verificação de Tipos
7 - Entrada de Dados
"""

# ==========================================
# PASSO 01 - TIPOS NUMÉRICOS
# ==========================================

# int -> Números inteiros
# float -> Números com casas decimais
# complex -> Números complexos

print("===== TIPOS NUMÉRICOS =====")

# EXEMPLO 01 - NÚMERO INTEIRO
numero_inteiro = 10

print("Valor:", numero_inteiro)
print("Tipo:", type(numero_inteiro))

print("-------------------------")

# EXEMPLO 02 - NÚMERO DECIMAL
numero_decimal = 3.14

print("Valor:", numero_decimal)
print("Tipo:", type(numero_decimal))

print("-------------------------")

# EXEMPLO 03 - NÚMERO COMPLEXO
numero_complexo = 2 + 3j

print("Valor:", numero_complexo)
print("Tipo:", type(numero_complexo))

print("-------------------------")

# ACESSANDO CADA PARTE DO NÚMERO
print("Parte real:", numero_complexo.real)
print("Parte imaginária:", numero_complexo.imag)

# Separação visual
print("\n")


# ==========================================
# PASSO 02 - CONVERSÃO DE TIPOS
# ==========================================

# EXEMPLO CLÁSSICO:
# Dados do usuário normalmente chegam como string

print("===== CONVERSÕES =====")

# float -> int
valor = int(3.9)

print("int(3.9):", valor)
print("Tipo:", type(valor))

print("-------------------------")

# string -> int
valor1 = "10"

print("Antes:", type(valor1))

valor2 = int(valor1)

print('int("10"):', valor2)
print("Tipo:", type(valor2))

print("-------------------------")

# int -> float
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


