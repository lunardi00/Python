"""

# Exercício 1:

for num in range (0, 5):
    num = num + 1
    produto = num*3
    print(produto)

# Exercício 2:

for num in range (1, 100+1):
    print (num)

num = 0

while num < 100:
    num = num + 1
    print (num)

# Exercício 3:

num = 11

while num > 0:
    num = num - 1
    print (num)
else:
    print('FIM!')

# Exercício 4:

num = int(0)

for num in range (num, num+100100, 1000):
    print(num)

# Exercício 5:

qtd = 10
soma = 0

for x in range(1, qtd+1):
    num = int(input(f'Escolha o valor {x}/{qtd}: '))
    soma = soma + num
print(f'A soma é {soma}')

# Exercício 6:

qtd = 10
soma = 0

for x in range (0, qtd):
    num = int(input(f'Escolha o valor {x}/{qtd}: '))
    soma = soma + num

media = soma / qtd
print(f'A média é {media}')

# Exercício 7:

qtd = 10
soma = 0

for _ in range(0, qtd):
    num = int(input(f'Digite o valor {_}/{qtd}: '))
    if num > 0:
        soma = soma + num

media = soma / qtd
print(f'A média é {media}')

# Exercício 8:

qtd = 10
maior = menor = 0

for num in range (1, qtd+1):
    valor = int(input(f'Digite o valor {num}/{qtd}: '))
    if num == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
print(f'O maior número é {maior} e o menor é {menor}')

# Exercício 9:

valor = int(input('Digite um número inteiro: '))

for num in range (1, valor+1, 2):
    print(num)

# Exercício 10:

qtd = 50
soma = 0

for num in range(2, qtd+1, 2):
    soma += num
print(soma)

# Exercício 47:

import time
option = 0

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

while option != 5:
    print('''    [1] adição
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [5] Sair''')
    print('')
    option = int(input('>>>>> Escolha uma opção: '))
    if option == 1:
        output = num1 + num2
        print(f' {num1} + {num2} = {output}')
    elif option == 2:
        output = num1 - num2
        print(f' {num1} - {num2} = {output}')
    elif option == 3:
        output = num1 * num2
        print(f' {num1} * {num2} = {output}')
    elif option == 4:
        output = num1 / num2
        print(f' {num1} / {num2} = {output}')
    elif option == 5:
        print('Finalizando o programa...')
    print('___' * 10)
    time.sleep(2)
    print('')
print('Fim do Programa!')

# Exercício 45:
import time
m_s = 0
km_h = 0
option = 0
km_h = int(input('Digite um valor para a velocidade (em Km/h): '))
m_s = int(input('Digite um valor para a velocidade (em M/s): '))

while option != 3:
    print('''
    [1] Conversão Km/h --> M/s
    [2] Conversão M/s  --> Km/h
    [3] Sair do Programa
    ''')
    option = (int(input('>>>>> Selecione uma opção: ')))
    if option == 1:
        conversão1 = km_h / 3.6
        print(f'{km_h} vale {conversão1} em M/s')
        m_s = conversão1
    elif option == 2:
        conversão2 = m_s * 3.6
        print(f'{m_s} vale {conversão2} em Km/h')
        km_h = conversão2
    elif option == 3:
        print('Finalizando o programa...')
    print('=-=-=-' * 10)
    time.sleep(2)
    print('''

        ''')
print('Fim do programa!')

"""

import time
option = 0

print('Bem vindo à Calculadora!')
time.sleep(1)
print('''

''')

num1 = int(input('Digite um número(1/2): '))
num2 = int(input('Digite um número(2/2): '))
print('''

''')

while option != 6:
    print('''    [1] Adição
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [5] Escolher novos números
    [6] Sair''')
    print('')
    option = int(input('>>>>> Escolha uma opção: '))
    if option == 1:
        output = num1 + num2
        print(f' {num1} + {num2} = {output}')
    elif option == 2:
        output = num1 - num2
        print(f' {num1} - {num2} = {output}')
    elif option == 3:
        output = num1 * num2
        print(f' {num1} * {num2} = {output}')
    elif option == 4:
        output = num1 / num2
        print(f' {num1} / {num2} = {output}')
    elif option == 5:
        num1 = int(input('Digite um número(1/2): '))
        num2 = int(input('Digite um número(2/2): '))
    elif option == 6:
        print('Finalizando o programa...')
    print('=-=-=' * 10)
    time.sleep(2)
    print('')
print('Fim do Programa!')
