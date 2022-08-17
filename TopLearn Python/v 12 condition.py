
# print("Enter you name")
# my_name = input()
# print(f"my name is {my_name}")

user_rank = 3
if user_rank == 1:
    print("you got GOLD medal")
elif user_rank == 2:
    print('you got SILVER medal')
elif user_rank == 3:
    print('you got BRONZE medal')
else:
    print('you don\'t have medal')

print("you got GOLD medal") if user_rank == 1 else print("no medal")
