# logical operators:
# and, or, not

user_age = 19
user_gender = 'male'

if user_age >= 18 and user_gender == 'male':
    print('you have to go to soldiery')
else:
    print('you can stay at home')

weather = 'rainy'

if weather == 'cloudy' or weather == 'sunny':
    print('we can travel')
else:
    print('we can not travel')

is_coming = False

# if ! is_coming:  # wrong
if not is_coming:  # correct
    print('is not coming')

# 2 < age < 8   => 2 dollars
# 65 <= age     => 5 dollars
# rest          => 10
age = 66
if 2 < age < 8:
    print(2)
elif 65 <= age:
    print(5)
else:
    print(10)
