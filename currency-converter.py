from requests import get
# pprint module - to better read data structures 
import pprint

BASE_URL = 'https://free.currconv.com/'
# >>>> Your API key here <<<<
API_KEY = 'YOUR KEY'


#  F to request data  to URL
def get_currencies():
        end_point = f'api/v7/currencies?apiKey={API_KEY}'
        url = BASE_URL + end_point
        data = get(url).json()['results']
        # pprint.pprint(data)
        data = list(data.items())
        data.sort()

        return data

def print_currencies(currencies):
        for name, currency in currencies:
                currency_name = currency['currencyName']
                currency_id = currency['id']
                currency_symbol = currency.get("currencySymbol", "")
                print(f"{currency_id} - {currency_name} - {currency_symbol}")

# currency data request and response 
def exchange_rate(currency1, currency2):
        end_point = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
        url = BASE_URL + end_point
        data = get(url).json()

        if len(data) == 0:
                print("Invalid currencies.")
                return

        rate = list(data.values())[0] 
        print(f"{currency1} -> {currency2} = {rate}")

        return rate

   
def convert(currency1, currency2, amount):
        rate = exchange_rate(currency1, currency2)

        if rate is None:
                return
        try:
            amount = float(amount)
        except:
              print("Invalid amount.")
              return
        
        converted_amount = rate * amount
        print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
        return converted_amount

def main():
        currencies = get_currencies()

        print("Welcome to the currency converter!")
        print("List - list of the different currencies")
        print("Convert - convert from one currency to another")
        print("Rate - get the exchange rate of two currencies")
        print()

        while True:
             command = input("Enter a command (q to quit):").lower()

             if command == "q":
                     break
             elif command == "List".lower():
                     print_currencies(currencies)  

             elif command == "Convert".lower():
                     currency1 = input("Enter currency id: ").upper()
                     amount = input(f"Enter an amount in {currency1}: ")
                     currency2 = input("Enter a currency to convert to: ").upper()
                     convert(currency1, currency2, amount)

             elif command == "Rate".lower():
                     currency1 = input("Enter currency id: ").upper()
                     currency2 = input("Enter a currency to convert to: ").upper()
                     exchange_rate(currency1, currency2)

             else:
                     print("Unrecognized command!")

main()
