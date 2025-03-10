'''

objetivos: receber a temperatura da carne e informar qual o ponto da carne dependendo da sua temperatura

'''

temperatura = int(input('Qual temperatura esta a carne? '))

if temperatura >= 71:
    print('A carne esta bem passada')
elif temperatura >= 65:
    print('A carne esta ao ponto para bem passado')
elif temperatura >= 60:
    print('A carne esta ao ponto')
elif temperatura >= 54:
    print('A carne esta ao ponto para mal passado')
elif temperatura >= 48:
    print('A carne esta selada')
else:
    print('A carne esta Crua')
