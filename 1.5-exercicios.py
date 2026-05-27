
# ======================================================
# ======================================================
# MÓDULO 1 — CRIAÇÃO DE STRINGS
# ======================================================

# EX1
# Crie uma variável chamada texto1 com o valor "Logica"
texto1 = "Logica"
print(texto1)

# EX2
# Crie uma variável chamada texto2 com o valor
# 'Eu sou top em python'
texto2 = 'Eu sou top em python'
print(texto2)

# EX3
# String com aspas duplas dentro
texto3 = 'copa "padrão fifa"'
print(texto3)

# EX4
# String com aspas simples dentro
texto4 = "copa 'padrão fifa'"
print 


# ======================================================
# MÓDULO 2 — STRINGS MULTILINHA
# ======================================================

# EX5
# String multilinha com menu
menu = """
-A Exibe ajuda
-E Execute agora, quero jogar!
"""
print(menu)

# EX6
# String multilinha com poema
poema = """
Hoje o dia está bonito
O céu está azul
E os pássaros cantam
"""
print(poema)


# ======================================================
# MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA
# ======================================================

# EX7
# Juntar as palavras automaticamente
print("Volei" " top!")

# EX8
# Concatenar strings automaticamente
print("Python" " é " "demais")


# ======================================================
# MÓDULO 4 — STRINGS COMO SEQUÊNCIAS
# ======================================================

# EX9
# Mostrar a primeira letra
st = "software"
print(st[0])

# EX10
# Mostrar a última letra
print(st[-1])

# EX11
# Mostrar do índice 1 até o 4
print(st[1:4])

# EX12
# Mostrar do início até o índice 3
print(st[:3])

# EX13
# Mostrar do índice 2 até o final
print(st[2:])

# EX14
# Mostrar o tamanho da string
print(len(st))

# EX15
# Mostrar o último caractere usando índice positivo
print(st[7])

# EX16
# Mostrar os índices pares
print(st[::2])

# EX17
# Inverter a string

# Inverter a string
print(st[::-1])