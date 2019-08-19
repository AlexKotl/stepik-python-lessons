import requests
from decimal import Decimal
from currency import convert

class FakeRequests:
    def get(self, url):
        with open('XML_daily.xml', 'r', encoding='utf-8', errors='ignore') as f:
            b = type('', (), {})()
            b.content = f.read()
            return b


fake_req = FakeRequests()
correct = Decimal('3754.8057')
result = convert(Decimal("1000.1000"), 'RUR', 'JPY', "17/02/2005", fake_req)
if result == correct:
    print("Correct")
else:
    print("Incorrect: %s != %s" % (result, correct))
