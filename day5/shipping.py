import iso6346

class ShippingContainer:
    next_serial = 1337

    '''@staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result'''

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents= None)

    @classmethod
    def create_with_items(cls, owner_code, *items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        self.serial = ShippingContainer._get_next_serial()


    def bic(self):
        return iso6346.create()






