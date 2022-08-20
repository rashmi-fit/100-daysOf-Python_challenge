import requests

country="United kingdom"

url= f"https://restcountries.com/v3/name/{country}"

response=requests.get(url)

print(f'Request is correctly sent {response}')

response_json=response.json()
print(response_json)

country_info = response_json[0]

# parsing

capital=country_info["capital"][0]
area=country_info["area"]
subregion=country_info["subregion"]

print(capital)
print(area)
print(subregion)