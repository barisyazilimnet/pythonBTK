import requests, json
api_url = "https://api.exchangeratesapi.io/latest?base="

sell_exchange = input("Bozdurulan döviz türü :")
receive_exchange = input("Alınacak döviz türü :")
quantity = int(input(f"Ne kadar {sell_exchange} bozdurmak istiyorsunuz :"))

result = requests.get(api_url + sell_exchange)
result = json.loads(result.text)
print(f"1 {sell_exchange} = {result['rates'][receive_exchange]} {receive_exchange}")
print(f"{quantity} {sell_exchange} = {quantity * result['rates'][receive_exchange]} {receive_exchange}")
print(f"{sell_exchange} dövizinİN son güncelleme tarihi {result['date']}")