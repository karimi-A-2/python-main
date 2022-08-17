class Chain:
    def __init__(self, param):
        if type(param) in [int, float]:
            self.value = float(param)
        elif type(param) is str:
            self.value = param
        else:
            raise Exception('invalid operation')
    
    def __call__(self, param):
        if (type(self.value) is str) and (type(param) is not str):
            raise Exception('invalid operation')
        if (type(self.value) is not str) and (type(param) is str):
            raise Exception('invalid operation')
        if type(param) is str:
            self.value += f' {param}'
        elif type(param) in [int, float]:
            self.value += float(param)
        else:
            raise Exception('invalid operation')
        return self
    
    def __eq__(self, other):
        return self.value == other

    def __repr__(self):
        if type(self.value) is float:
            if float(self.value).is_integer():
                return f'{int(self.value)}'
            return f'{self.value}'
        return f"'{self.value}'"
    

if __name__ == '__main__':
    # chain_ = Chain(3)(1.5)(2)(3)
    # chain_ = Chain('2')('3')('4')
    # chain_ = Chain(2)(3)(4)('a')
    chain_ = Chain(2)(3)(4)
    print(chain_)
    print(chain_ == '2 3 4')
    print(type(3.14))
    print(type(3))
    