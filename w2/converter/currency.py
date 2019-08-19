from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp', {'date_req': date})
    soup = BeautifulSoup(response.content, 'xml')
    # print(soup.prettify())
    data = {}
    for cur in (cur_from, cur_to):
        if cur == 'RUR':
            data.update({ cur: {
                'value': Decimal(1),
                'nominal': 1
            } })
        else:
            data.update({ cur: {
                'value': Decimal(soup.find('CharCode', text=cur).find_next_sibling('Value').string.replace(',', '.')),
                'nominal': int(soup.find('CharCode', text=cur).find_next_sibling('Nominal').string)
            } })
    result = amount * data[cur_from]['nominal'] * data[cur_from]['value'] / data[cur_to]['value'] * data[cur_to]['nominal']
    return Decimal(result).quantize(Decimal('1.0000'))
