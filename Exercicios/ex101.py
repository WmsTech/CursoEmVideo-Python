def voto(ano=0):
    idade = 0
    from datetime import date
    idade = date.today().year - ano
    if idade < 0 or ano == 0:
        return 'NEGADO'
    else:
        if 18 <= idade < 65:
            return f'Com a idade de {idade} anos: VOTO OBRIGATORIO!'
        elif idade >= 65 or 16 <= idade < 18:
            return f'Com a idade de {idade} anos: VOTO OPCIONAL!'
        else:
            return f'Com a idade de {idade} anos: NÃO VOTA!'


nasc = int(input('Digite o ano do seu nascimento: '))
print(voto(nasc))