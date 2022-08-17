try:
    print(name)
except:  # correct but # PEP 8: E722 do not use bare 'except'
    print('name undefined')
