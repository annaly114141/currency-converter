import sys
from sys import argv
from api import call_api, format_latest_url
from currency import check_valid_currency, extract_api_result


def main():
    """
    Function that will check if there are enough input arguments provided.
    If so it will return the formatted result from the Frankfurter app.
    If not it will return an error message

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # => To be filled by student
        using .argv from systems package
        n=length of argv
        if(n<3)
        print error
        elif(data not returned)
        print error
        

    Returns
    -------
    str
        Formatted API result or error message
    """
    # => To be filled by student
    n = len(sys.argv)
    if(n<3):
        print("[ERROR] You haven't provided 2 currency codes")
    else:
        from_currency=argv[1]
        to_currency=argv[2]
        get_rate(from_currency, to_currency)


    return None


def get_rate(from_currency: str, to_currency: str):
    """
    Function that will check if provided currency codes are valid otherwise it will return error message.
    If both are valid, it will format the API url, make a request to it and format the result

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    # => To be filled by student
        if(to_currency and from_currency)==True
        requesturl=format_latest_url(from_currency, to_currency)
        response=call_api(reurl)
        data=response.json
        send extracted api function for formatting the response
        extract_api(data)

    Returns
    -------
    str
        Formatted API result or error message
    """
    # => To be filled by student

    if(check_valid_currency(from_currency) is True and check_valid_currency(to_currency) is True):
        latest_url= format_latest_url(from_currency,to_currency)
        response=call_api(latest_url)
        latest_data=response.json()
        #print(latest_data)
        if (response.status_code == 200):
            print("The request was a success!")
            extract_api_result(latest_data)
            
        else:
              print("ERROR No RESULT FOUND")
    elif(check_valid_currency(from_currency) is False):
        print(str(from_currency)+" is not a valid option")
    else:
        print(str(to_currency)+" is not a valid option")


    return None


if __name__ == "__main__":
    main()
