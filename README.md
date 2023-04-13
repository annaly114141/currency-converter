<h1 align="center">Currency Converter</h1>

## Author

**Full Name**
Anna Ly

## Available Commands

In the project directory, you can run:

### `python3 main.py GBP AUD`,

If you are using Pipenv, then you can run:

### `pipenv python3 main.py AUD EUR`,

## Built With

- Python3

## Package Dependencies

```bash
import requests
```

## Structure

```
├── api.py             <- script contains the code for calling API endpoints 
├── currency.py        <- contains the code for checking if currency code is valid, store results and format final output
├── main.py            <- main program used for entering the input parameters (currency codes) and display the results
├── Pipfile            <- contain information for the dependencies of the project
├── Pipfile.lock       <- specify, based on the packages present in Pipfile
├── README.md          <- a markdown file containing student details, a description of this project, listing of all Python functions and classes and instructions for running the code
├── test_api.py        <- python script for testing code from api.py
└── test_currency.py   <- python script for testing code from currency.py
```
