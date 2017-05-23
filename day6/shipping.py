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
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code, contents= None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, *items, **kwargs):
        '''
        Create a container with many items.
        :param owner_code: 3 letter owner code.
        :param items: A list of items in the container.
        :param kwargs:  optional keyword arguements.
        :return: the container.
        '''
        return cls(owner_code, contents=list(items), **kwargs)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))


    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        #self.serial = ShippingContainer._get_next_serial()
        self.bic = self._make_bic_code(owner_code=owner_code,
                                                    serial= self._get_next_serial() )


class RefrigeratorShippingContainer(ShippingContainer):

    max_temp = 4.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
            serial=str(serial).zfill(6), category='R')

    def __init__(self, owner_code, contents, temp):
        '''
        Create a Refrigerated Shipping Container.
        :type temp: object
        :param owner_code: 3 letter owner code.
        :param contents: contents of the container.
        :param temp: Set point temperature of the refrigerator.
        '''
        super().__init__(owner_code, contents)
        #self.temperature(temp)
        if temp > RefrigeratorShippingContainer.max_temp:
            raise ValueError("Temperature is too hot.")
        self._temperature = temp

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temp):
        if temp > RefrigeratorShippingContainer.max_temp:
            raise ValueError("Temperature is too hot.")
        self._temperature = temp

def main():
    rs1 = RefrigeratorShippingContainer.create_with_items("ETE", "vegetables", "meat", "milk", temp = 2.4)
    print(rs1)
    print(rs1._contents)
    print(rs1.bic)
    print(rs1._temperature)

if __name__ == '__main__':
    main()
    exit(0)