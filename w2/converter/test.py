import requests
from decimal import Decimal
from currency import convert

class FakeRequests:
    def get(self, url):
        with open('xml/26_02_2017.xml', 'r', encoding='utf-8', errors='ignore') as f:
            b = type('', (), {})()
            b.content = f.read()
            return b


fake_req = FakeRequests()

correct = Decimal('1051.8006')
result = convert(10**3, 'EUR', 'USD', "26/02/2017", requests)

# correct = Decimal('3754.8057')
# result = convert(Decimal("1000.1000"), 'RUR', 'JPY', "17/02/2005", requests)

if result == correct:
    print("Correct")
else:
    print("Incorrect: %s != %s" % (result, correct))
