import requests
import json

response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

print(response)
print(response.json())
items = response.json()['items']
for element in items:
    print(element)

for question in response.json()['items']:
    if question['answer_count'] == 0:
        print(question['title'])
        print(question['link'])
    else:
        print('skipped')
    print()
