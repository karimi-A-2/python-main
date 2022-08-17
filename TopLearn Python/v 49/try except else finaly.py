while True:
    try:
        num = int(input("plese enter a number: "))
    except ValueError:
        print("except: ValueError: that's not a number! please enter another one :")
    else:
        print('else')
        break
    finally:
        print('finally')
