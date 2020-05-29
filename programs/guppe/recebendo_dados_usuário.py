"""
Recebendo dados usuário

input() -> Todo dado recebido via input é do tipo String

Em python, String é tudo que estuver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

"""
# Entrada de dados
nome = input('Qual seu nome?')
print(f'Bem-vindo {nome}')
idade = int(input('Qual sua idade? '))

# Processamento


# Saída de dados
print(f'O {nome} tem {idade} anos ')
print(f'O {nome} nasceu em {2019 - idade}')
