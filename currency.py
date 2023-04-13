from dataclasses import dataclass
from api import get_currencies

CURRENCIES = get_currencies()
#print currencies
flag=0

def check_valid_currency(currency: str) -> bool:
    """
    Function that will check currency code is amongst the list of available currencies

    Parameters
    ----------
    currency : str
        Currency code to be checked

    Pseudo-code
    ----------
    # => To be filled by student
    We use flag to determine whether or not something had happened and condition met was in an algorithm.
    Later we check value of variable to act on it. In this case, we are checking if the currency code is amongst the list of currencies.


        dictionarylist=get_currencies
        for i(until length of list):
            if(list[i]==selected_currency)
            flag=1
            return true
            else
            return false

    Returns
    -------
    bool
        True if the currency code is valid otherwise False
    """

    # => To be filled by student
    for i in range(0,len(CURRENCIES)):
        if(CURRENCIES[i] == currency):
            global flag
            flag=1
            #print("valid currency")
            return True
    if(flag==0):
        return False


@dataclass
class Currency:
    """
    Class that represents a Currency conversion object. 

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    """
    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate, round it to 5 decimal places and save it in the attribute inverse_rate

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # => To be filled by student

        self.inverse_rate=round(self.amount*(1/self.rate),5)
        #print(self.amount,self.rate)

    def format_result(self):
        """
        Methods returning the formatted successful message

        Parameters
        ----------
        None

        Returns
        -------
        str
            Formatted successful message
        """
        # => To be filled by student
        print("Today's "+"("+self.date+")"+ " conversion rate from "+ str(self.from_currency)+" to "+str(self.to_currency)+" is "+str(self.rate)+".The inverse rate is "+str(self.inverse_rate))
        

        return None


def extract_api_result(result: dict) -> Currency:
    """
    Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and
    calculate the inverse rate

    Parameters
    ----------
    result : dict
        Results of the API converted as dictionary

    Pseudo-code
    ----------
    # => To be filled by student
        cc=class currency
        cc.date= response.date
        cc.rate=response.rate
        cc.amount=response.amount
        cc.to_currency=repsonse.to_currency
        cc.from_currency=response.from_currency
        send to self function to dispaly info
        cc.reverse_rate()
        cc.formated_result

    Returns
    -------
    Currency
        Instantiated Currency
    """
    # => To be filled by student
    c1=Currency()
    Currency.date=result["date"]
    c1.date=result["date"]
    currency_names=result["rates"].keys()
    list_currency=list(currency_names)
    #print(c1.date)
    #print(result)
    c1.from_currency=list_currency[1]
    #print(c1.from_currency)
    c1.to_currency=list_currency[0]
    #print(c1.to_currency)
    c1.amount=result["amount"]
    Currency.amount=c1.amount
    #print(c1.amount)
    result_rate=result["rates"].values()
    list_rate_values=list(result_rate)
    Currency.rate=list_rate_values[0]
    c1.rate=list_rate_values[0]
    c1.reverse_rate()
    c1.format_result()
    return c1.amount,c1.rate,c1.date


