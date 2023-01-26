my_numbers = [1, 2, 3, 4, 5]
print(my_numbers)
# dictionary = {
#     key : value
# }

my_dictionary = {
    'name': 'item 1',
    'count': 3,
    'price': 2500,
    3: True,
    '3': False,
}
print(my_dictionary)
print(my_dictionary[3])
print(my_dictionary["3"])
# print(my_dictionary['key_4'])  # KeyError: 'key_4'

my_shopping_cart = [
    {
        'name': 'python',
        'price': 'free'
    },
    dict(name='kotline', price=2500)
    # {
    #     'name': 'kotlin',
    #     'price': 2500
    # }
]
print(my_shopping_cart)
print(my_shopping_cart[0]['name'])
print(my_shopping_cart[0]['price'])
print(my_shopping_cart[1]['name'])
print(my_shopping_cart[1]['price'])

my_dictionary_2 = dict(key1='v1', key2='v2', key_n='vn')
print(my_dictionary_2)
print(my_dictionary_2['key_n'])
print(my_dictionary_2['key2'])
