def gen_ticket_number(count, series, length=6):
    """
    генератор номеров билетов, входные параметры: count - количество билетов,
    series - номер серии, необязательный аргумент length - количество цифр
    в номере, по умолчанию равен 6, выход - строка вида: <номер билета> <серия билета>
    """
    
    series_gen = gen_series(series)
    number_gen = gen_number(length)
    
    total = 0
    for serie in gen_series(series):
        for number in gen_number(length):
            if total >= count:
                return
            total += 1
            yield number + ' ' + serie


def gen_series(series):
    """
    генератор серий лотерейных билетов начиная с series по "ZZ" включительно, входные 
    параметры: series -  - номер серии, выход - строка, состоящая из двух заглавных 
    букв латинского алфавита
    """
    
    series = series.upper()
    while series != 'ZZ':
        yield series
        if series[1] == 'Z':
            series = chr(ord(series[0]) + 1) + 'A'
        else:
            series = series[0] + chr(ord(series[1]) + 1)
    yield series # output last series


def gen_number(length=6):
    """
    генератор номеров лотерейных билетов в одной серии, входные параметры: 
    необязательный аргумент length - количество цифр в номере, по умолчанию равен 6
    """
    
    number = 0
    while number < 10**length - 1:
        number += 1
        yield f'{number:0{length}d}'

for number in gen_ticket_number(1000, 'DD'):
    print(number)