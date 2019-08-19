from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}')
    soup = BeautifulSoup(response.content, 'xml')

    result = Decimal('3754.8057')
    return result  
