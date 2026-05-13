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

# EXEMPLO 03 - ACESSANDO CADA PARTE DO NÚMERO 

# .real retorna a parte imaginaria 
print ("Parte Imaginária:" , numero_complexo.real)

# .imag retorna a parte imaginária
print ("Parte imaginária : ", numero_complexo.imag)

# APENAS PARA SEPARAR VISUALMENTE A SAIDA 
print ("\n\n")

#=======================================
  ##  PASSO 02 - CONVERSÃO TIPOS
#=======================================

# emxemplo Clássico
# Dados vindos do usuários  são texto (string) , muitas vezes é necessário converter eles .

print ("====== Conversões ======")

# float -> int (3.9)

valor  = int (3.9)

print("int(3.9) :", valor)
print("tipo:", type(valor))

# string -> int
valor1 = "10" 
print(type(valor1))

valor2 = int ("10")
print = ('int("10"):', valor2)
print ("tipo:", type(valor2))

#int --> Float
valor3 = float (10)
print("float(10:", valor3)
print("tipo:", type(valor3))

