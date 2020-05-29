
# Teoria
"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

# Em C
for (int i = 0, int < 10, int ++
{
    //execução do loop
}

# Em Python
for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequencias ou valores iteráveis

Exemplos de iteráveis:
- String
- Lista
    lista = [1, 3, 5, 7 ,9]
- Range
    numeros = range(1, 10)

"""

# Código
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de For 1 (Iterando em uma string):
for letra in nome:
    print(letra)

# Exemplo de For 2 (Iterando sobre uma lista):
for numero in lista:
    print(numero)

# Exemplo de For 3 (Iterando sobre um range):
for numero in numeros:
    print(numero)
    nome = 'Geek University'


OBS: Valor final não é incluído

# Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), ...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor podemos descartá-los usando underline

for valor in enumerate(nome):
    print(valor)

# Exemplo de For 4:
qtd = int(input(f'Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Escolha o valor {n}/{qtd}: '))
    soma = soma + num
print(f'A soma é {soma}')

# Exemplo de For 5:
nome = 'Geek University'
for letra in nome:
    print(letra, end='')
"""

