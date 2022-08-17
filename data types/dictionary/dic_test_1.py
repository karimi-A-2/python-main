from typing import Dict

if __name__ == '__main__':
    a_dict = {'one': 3}  # Here 'one' is the key.
    pop = a_dict.pop('one')
    print(pop)
    dict_2: Dict[str, int] = {'one': 1}  # Here 'one' is the key.
    # dict_2.get()
