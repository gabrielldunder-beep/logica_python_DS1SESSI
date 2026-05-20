# EX1
# Use a função type() para verificar
# o tipo da variável "ano" com valor 2024.
ano = 2024
print(type(ano))


# EX2
# Verifique se o número 3.14159
# é do tipo float usando isinstance().
numero = 3.14159
print(isinstance(numero, float))
print(type(numero))


# EX3
# Compare se o tipo de 100
# é igual ao tipo de True.
print(type(100) == type(True))


# EX4
# Use isinstance() para verificar
# se True pode ser considerado int.
print(isinstance(True, int))
print(type(True))


# EX5
# Verifique se o resultado de 5/2
# é do tipo float usando type() e isinstance().
resultado = 5/2
print(type(resultado))
print(isinstance(resultado, float))


# EX6
# Crie uma função que recebe um valor
# e imprime "É número!" se for int, float ou complex.
def verificar_numero(valor):
    print("Tipo:", type(valor))
    if isinstance(valor, (int, float, complex)):
        print("É número!")
    else:
        print("Não é número!")

# Testes
verificar_numero(10)
verificar_numero(3.5)
verificar_numero(2+3j)
verificar_numero("texto")


# EX7
# Compare type() e isinstance()
# para verificar se um booleano
# é considerado inteiro.
print(type(True) == int)          # comparação direta
print(isinstance(True, int))     # verifica herança
print(type(True))


# EX8
# Descubra o tipo do número 3+4j
# usando type().
num_complexo = 3+4j
print(type(num_complexo))


# EX9
# Verifique se o valor None
# é do tipo NoneType usando isinstance().
valor = None
print(isinstance(valor, type(None)))
print(type(valor))


# EX10
# Verifique se o número 3.0
# é int, float ou complex usando isinstance()
# e depois teste especificamente se é int.
num = 3.0
print(type(num))
print(isinstance(num, (int, float, complex)))
print(isinstance(num, int))