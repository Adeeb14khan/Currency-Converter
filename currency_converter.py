import requests

def convert_currency(amount, from_currency, to_currency):
    # Free API from ExchangeRate-API 
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if to_currency not in data["rates"]:
        return "Invalid currency code!"
    
    rate = data["rates"][to_currency]
    converted_amount = amount * rate
    return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"

print(convert_currency(100, "USD", "INR"))  # Converts 100 USD to INR
