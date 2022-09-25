base = 1024
kilo = base
mega = base ** 2
giga = base ** 3
tera = base ** 4
peta = base ** 5

def formata_tamanho(tamanho):

    if  tamanho < kilo:
        sigla = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        sigla = 'K'
    elif tamanho < giga:
        tamanho /= mega
        sigla = 'M'
    elif tamanho < tera:
        tamanho /= giga
        sigla = 'G'
    elif tamanho < peta:
        tamanho /= tera
        sigla = 'T'
    else:
        tamanho /= peta
        sigla = 'P'
    
    return f'{round(tamanho)}{sigla}'