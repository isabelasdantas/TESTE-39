from datetime import date
nome = int(input('Em que ano você nasceu: '))
atual = date.today().year
idade = atual - nome
print('Quem nasceu em {} tem {} anos de idade em {}.'.format(nome, idade, atual))
if idade == 18:
    print("Você deve se alistar IMEDIATAMENTE!")
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos atrás.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
else:
    saldo = 18 - idade
    print('Você deve se alistar daqui {} anos!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))