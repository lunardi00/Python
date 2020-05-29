
# Teoria
"""
Range

São utilizados para gerar sequencias numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais:

# Forma 1
range(valor_de_parada)

OBS: valor_de_parada não inclusive (ínicio padrão 0, e passo de 1 em 1)

# Exemplo Forma 1:
for num in range(11):
    print(num)

# Forma 2:
range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (ínicio informado pelo usuário, e passo de 1 em 1)

# Exemplo Forma 2:
for num in range(4, 11):
    print(num)

# Forma 3:
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (ínicio informado pelo usuário, e passo informado pelo usuário)

# Exemplo Forma 3:
for num in range (5, 50, 5):
    print(num)

# Forma 4 (Inversa):
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (ínicio informado pelo usuário, e passo informado pelo usuário)

# Exemplo Forma 4:
for num in range(10, 0, -1):
    print(num)
"""