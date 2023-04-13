import unittest
from api import call_api, format_currencies_url, get_currencies, format_latest_url, _HOST_, _LATEST_, _CURRENCIES_

#testing if code works...


class TestFormatUrl(unittest.TestCase):
    def test_function(self):
        # => To be filled by student
        b=format_currencies_url()
        a =_HOST_+_CURRENCIES_
        c =_HOST_+_LATEST_+ ("?to=USA, AUD")
        d =format_latest_url("USA","AUD")
        self.assertEqual(a, b)
        self.assertEqual(c, d)

class TestAPI(unittest.TestCase):
    def test_function(self):
         # => To be filled by student
        a=call_api(format_currencies_url())
        b=200
        c=call_api(format_latest_url("usa","AUD"))
        d=200
        print(c)
        self.assertEqual(a.status_code, b)
        self.assertEqual(c.status_code, d)
