"""
Estruturas Condicionais - If, Else, Elif
"""

idade = 6

"""
#Condicional em C:

if(idade < 18){
    printf("Menor de idade");
}
else if (idade == 18){
    printf("Tem 18 anos");
}
else{
    printf("Maior de idade);
}
"""

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
