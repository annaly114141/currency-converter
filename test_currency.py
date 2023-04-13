import unittest
from currency import check_valid_currency, extract_api_result, Currency


class TestValidCurrency(unittest.TestCase):
    def test_function(self):
        # => To be filled by student
        a="USD"
        b="AUD"
        c=check_valid_currency(a)
        d=check_valid_currency(b)
        self.assertEqual(c, d)



class TestExtractApi(unittest.TestCase):
    def test_function(self):
        # => To be filled by student
        b=extract_api_result({'amount': 1.0, 'base': 'EUR', 'date': '2021-09-09', 'rates': {'AUD': 1.6035, 'USD': 1.1838}})
        print(list(b))
        a=[float(Currency.amount),float(Currency.rate),str(Currency.date)]
        ls_a=list(a)
        ls_b=list(b)
        self.assertEqual(ls_a, ls_b)

if __name__ == '__main__':
    unittest.main()
