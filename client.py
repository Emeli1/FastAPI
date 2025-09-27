import requests


response = requests.post('http://localhost:8000/advertisement',
                        json={"title": "продам куртку", "description": "новое", "price": 3000, "owner": "Вася Пупкин"})
print(response.text)
print(response.status_code)

# response = requests.get('http://localhost:8000/advertisement/6')
# print(response.text)
# print(response.status_code)

response = requests.get('http://localhost:8000/advertisement/', params={"price": 3000})
print(response.text)
print(response.status_code)

# response = requests.patch('http://localhost:8000/advertisement/1', json={"price": "5000"})
# print(response.text)
# print(response.status_code)
#
# response = requests.get('http://localhost:8000/advertisement/1')
# print(response.text)
# print(response.status_code)

# response = requests.delete('http://localhost:8000/advertisement/1')
# print(response.text)
# print(response.status_code)

# response = requests.get('http://localhost:8000/advertisement/1')
# print(response.text)
# print(response.status_code)