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

# AULA COMPLETA - STRINGS EM PYTHON

# - Criação de strings
# - Strings multilinha
# - Índices e slices
# - Operações com strings
# - imutabilidade
# - Métodos úteis
# - Formação de texto 
# - unicode e bytes

#------------------------
# 1) CRIAÇÃO DE STRINGS
#------------------------
 # Strings são textos em python
 # Podem ser criadas usando aspas simples ou duplas 

texto1 = "Python"
texto2 = 'curso de python'
texto3 = "copa 'padrão fifa'"
texto4 = 'copa "padrão fifa"'

print(texto1,texto2,texto3,texto4)

# Pyton permite misturar aspas simples ou duplas,dentro das strings sem precisar escapar caracteres

#------------------------------------
# 2) Strings multilinha
#------------------------------------
# usando trés aspas ("""ou ''') para criar textos que ocupam várias linhas.

menu = """\
Uso:ograma [OPÇÕES]
-H Exibe ajuda
-U url do dataset
"""
print(menu)

#ESSE formato é muito usada para:
# - Menus
# - Documentação
# - textos longos

#---------------------------
# 3) concatenação automática
#-----------------------------
# Quandos duas strings aparecem lado a lado, o python junta automaticamente

texto = ("copa" "2026" "Neymar é show mesmo? " "talvez")
print (texto)

#----------------------------
# 4) strings como sequência de caracteres, cada caractere possui um índice

st = "maracana"
print ("primeira letra", st[0])
# só exibir a letra: m

print ("ultima letra", st[-1])

print ("trecho 1:4", st[1:4])

print ("do inicio até 3:", st[:3])

print ("do 2 até o fim:", st[2:])

print ("tamanho", len(st))
