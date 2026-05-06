# AULA COMPLETA : NUMEROS EM PYTHON
"""
VAMOS APRENDER :
1 - tipos numéricos
2 - conversões de tipos
3 - Hierarquia numérica
4 - operações matemáticas
5 - Coerção de tipos 
6 - verificação de tipos 
7 - Entradasa de dados 
"""
#==========================
# PASSO 01 - TIPOS NUMÉRICOS
#==========================
# int -> números inteiros 
# float -> números com casas decimais 
# complex -> números complexos (usado em matemática/engenharia)

print("===== TIPOS NUMÉRICOS =====")

# EXEMPLO O1 - NUMERO INTEIRO

# criamos uma variável chamada numero_inteiro
numero_inteiro = 10

#Mostramos o valor
print ("valor:" , numero_inteiro)

#type () mostra qual é o tipo de variável
print("Tipo:", type(numero_inteiro))

print ("====================")

# EXEMPLO 02 - NUMERO DECIMAL 

numero_decimal = 3.14

print ("valor", numero_decimal)
print ("Tipo", type(numero_decimal))


print ("========================")

# EXEMPLO 03 - NUMEROS COMPELXOS
# um numéro complexo posssui duas partes:
# Parte real (Numero normal)
# Parte imaginária (multiplicada por j)

# Estrutura Geral :
# numero = a + bj

# a = parte real
# b = parte imaginária
# j = unidade imaginária

numero_complexo = 2 + 3j

print("valor:", numero_complexo)
print ("Tipo:", type(numero_complexo))

print("================")
