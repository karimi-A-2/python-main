class CostumeError(ValueError):
    
    def __init__(self, list_) -> None:
        super().__init__()
        self.list_ = list_


try:
    raise CostumeError([1, 2])
except CostumeError as err:
    print(err.list_)

