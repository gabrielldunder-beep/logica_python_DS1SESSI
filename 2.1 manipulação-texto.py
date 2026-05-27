
# AULA COMPLETA - STRING EM PYTHON

# - Criação de Strings 
# - Strings multilinha
# - Indices e slices 
# - Operações com Strings 
# - Imutabilidade
# - Métodos úteis 
# - Formatação de Texto 
# - Unicode e Bytes

#-------------------------------------------
# 1) CRIAÇÃO DE STRINGS 
#-------------------------------------------
# Strings são textos em Python
# Podem ser criadas usando aspas simples ou duplas

texto1 = "python"
texto2 = 'curso de python'
texto3 = "Copa 'Padrão fifa'" 
texto4 = 'Copa "Padrão FIFA"'

print(texto1, texto2, texto3, texto4)
# Python permite misturar aspas simples e duplas dentro das strings sem precisar escapar caracteres

#-----------------------------------------------
# 2) STRINGS MULTILINHA
#-----------------------------------------------
# Usando três aspas (""" ou ''') para criar textos que ocupam várias linhas.

menu = """\
uso: programa [OPÇÕES]
-H Exibe Ajuda 
-U Url do dataset
"""
print(menu)

# - Esse formato é muito usado para:
# - Menus 
# - Documentação (Docstrings)
# - Textos longos 

#-----------------------------------------------
# 3) CONCATENAÇÃO AUTOMÁTICA 
#-----------------------------------------------
# Quando duas ou mais strings aparecem lado a lado entre parênteses, elas se juntam automaticamente 

texto = ("copa " "2026 " "Neymar é show mesmo " "SIM")
print(texto)

#-----------------------------------------------
# 4) STRINGS COMO SEQUÊNCIAS (ÍNDICES E SLICES)
#-----------------------------------------------
# Uma string funciona como uma sequência de caracteres. Cada caractere possui um índice.

st = "Maracanã"
print("Primeira Letra:", st[0])   # Exibe a letra: M (Maiúscula)
print("Última Letra:", st[-1])     # Exibe a letra: ã

print("Trecho 1:4:", st[1:4])     # Retorna: ara (índices 1, 2 e 3)
print("Do início até 3:", st[:3])  # Retorna: Mar (índices 0, 1 e 2)
print("Do 2 até o fim:", st[2:])   # CORRIGIDO: Retorna: racanã (do índice 2 em diante)
print("Tamanho:", len(st))         # Retorna a quantidade de caracteres: 8

#-----------------------------------------------
# 5) OPERAÇÕES COM STRINGS
#-----------------------------------------------
# Python permite várias operações com strings

print("m" in st)      # Retorna False (pois no "Maracanã" o M é maiúsculo)
print("M" in st)      # Retorna True
print("x" not in st)  # Retorna True (Significa que "x" realmente não existe na string)

print("m" * 3)        # Multiplicação repete a string: mmm
print("m" + "aracanã") # Operador + concatena strings: maracanã

#-----------------------------------------------
# 6) STRINGS SÃO IMUTÁVEIS
#-----------------------------------------------
# Strings não podem ser alteradas diretamente!
# Isso significa que o conteúdo original não muda, o que acontece é a criação de uma nova string.

texto5 = "python 3" 

# CORRIGIDO: Aplicado na variável correta (texto5)
texto5 = texto5.replace("3", "2") 
print(texto5) # Retorna: python 2

#----------------------------------------------
# 7) MÉTODOS IMPORTANTES 
#-----------------------------------------------
# Strings possuem vários métodos úteis. 
 
cidade = "maracana" 

# Coloca a primeira letra em maiúscula
print(cidade.capitalize()) # Retorna: Maracana

# Conta quantas vezes a letra "a" aparece
print(cidade.count("a"))   # Retorna: 3

# Verificar se começa com "m"
print(cidade.startswith("m")) # Retorna: True

# CORRIGIDO: Corrigida a grafia de endswith
# Verifica se termina com "z" 
print(cidade.endswith("z")) # Retorna: False

frase = "copa de 2002"

#Divide a string em uma lista 
print(frase.split(""))

#------------------------------
# 8) FORMATAÇÃO DE STRINGS
#-------------------------------