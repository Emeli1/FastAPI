import requests


response = requests.post('http://localhost:8000/advertisement',
                        json={"title": "куплю пальто", "description": "новое", "price": 2000, "owner": "Вася Пупкин"})
print(response.text)
print(response.status_code)
#
# response = requests.get('http://localhost:8000/advertisement/9')
# print(response.text)
# print(response.status_code)

# response = requests.get('http://localhost:8000/advertisement/', params={"title": "продам куртку", "price": 2000})
# print(response.text)
# print(response.status_code)

# response = requests.patch('http://localhost:8000/advertisement/1', json={"title": "продам жилетку"})
# print(response.text)
# print(response.status_code)
#
# response = requests.get('http://localhost:8000/advertisement/1')
# print(response.text)
# print(response.status_code)

# response = requests.delete('http://localhost:8000/advertisement/1')
# print(response.text)
# print(response.status_code)

response = requests.get('http://localhost:8000/advertisement/1')
print(response.text)
print(response.status_code)