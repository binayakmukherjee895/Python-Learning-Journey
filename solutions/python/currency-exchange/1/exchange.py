"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    return budget/exchange_rate
     

def get_change(budget, exchanging_value):
    return budget-exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return denomination*number_of_bills


def get_number_of_bills(amount, denomination):
    return amount//denomination
   

def get_leftover_of_bills(amount, denomination):
    return amount%denomination
  

def exchangeable_value(budget, exchange_rate, spread, denomination):
    exchange_fee=exchange_rate*spread/100
    actual_rate=exchange_fee+exchange_rate
    foreign_currency= budget/actual_rate
    no_of_notes=foreign_currency//denomination
    exchangeable_amt=no_of_notes*denomination
    return exchangeable_amt
    
   