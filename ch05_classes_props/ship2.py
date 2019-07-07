class ShippingContainer:
    
    next_serial = 1
    
    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result
    
    def __init__(self, ownercode, contents):
        self.ownercode = ownercode
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()