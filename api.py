import requests
_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'



response=""
currency_url=""
latest_url=""

def call_api(url: str) -> requests.models.Response:
    """
    Function that will call the specified API endpoint and return the response

    Parameters
    ----------
    url : str
        URL of the API endpoint to be called

    Pseudo-code
    ----------
    # => To be filled by student
        response=get request from _HOST_
        return response

    Returns
    -------
    requests.models.Response
        Response from API request
    """
    # => To be filled by student
    global response
    response = requests.get(url)

    return response

def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # => To be filled by student
        hosturl =https://api.frankfurter.app
        currencies=/currencies
            needed_url=https://api.frankfurter.app/currencies
        so
        cocatenate both variables to get needed_url by
        needed_url=hosturl+currencies
        now we call to api by the api fucntion using new url
        call_api(needed_url)

    Returns
    -------
    str
        Formatted URL to the currency endpoint
    """
    # => To be filled by student
    global currency_url
    currency_url=_HOST_+_CURRENCIES_
##    print("url is:"+currency_url)

    return currency_url


def get_currencies():
    """
    Function that will extract the currency codes available from the Frankfurter app as a list

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # => To be filled by student
        When this function is called, we use response given from call_api function to analyse/process the data.
        Since data is in a .json format so we can use .json function to extract data
        .json format is in a dictionary so we use keys with currency codes being the keys.
        We extract them using
         d=resp.json()
        keylist=data.keys()
        now convert the keylist to a list from dictionary by
        type casting
        list(data.keys) and return list


    Returns
    -------
    list
        Currency codes available from the Frankfurter app
    """
    # => To be filled by student
        # => To be filled by student
    format_currencies_url()
    call_api(currency_url)
    data=response.json()
    keys_list=data.keys()
    list_currency=list(keys_list)
    #print(list_currency)

    return list_currency




def format_latest_url(from_currency: str, to_currency: str) -> str:
    """
    Function that will format the URL to the latest endpoint

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    # => To be filled by student
        this function is used to send 'to' command to extract the current rate of defined currencies
        latesturl=host+to=from_currency,to_currency
        return
        latesturl


    Returns
    -------
    str
        Formatted URL to the latest endpoint
    """
    # => To be filled by student

    global currency_url
    latest_url=_HOST_+_LATEST_+"?to="+from_currency+","+to_currency
    #print(latest_url)
    return latest_url


