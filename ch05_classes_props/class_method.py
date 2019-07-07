import iso6346

class ShippingContainer:
    
    next_serial = 1
    
    def __init__(self, ownercode, contents):
        self.ownercode = ownercode
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()
        self.bic = self._make_bic_code(owner_code= ownercode, serial=self.serial) 
        # self._make_bic_code when we need polymorphic dispatch
    
    @classmethod    
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result
    
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code = owner_code, serial = str(serial).zfill(6))
    
    @classmethod
    def create_empty(cls, *args, **kwargs):
        return cls(owner_code, contents = None, *args, **kwargs)
    
    @classmethod
    def create_list(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, contents = list(items), *args, **kwargs)
    
class RefrigeratedShippingContainer(ShippingContainer):
    
    MAX_CELSIUS = 4.0
    
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code = owner_code, serial = str(serial).zfill(6), category = 'R')
    
    def __init__(self, ownercode, contents, celsius):
        super().__init__(ownercode, contents)
        if(celsius > RefrigeratedShippingContainer.MAX_CELSIUS) :
            raise ValueError("Temperature too hot")
        self.celsius = celsius