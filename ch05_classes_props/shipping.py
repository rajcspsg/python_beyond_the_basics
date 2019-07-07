class ShippingContainer:
    next_serial = 1337 # class attribute
    
    def __init__(self, ownercode, contents):
        self.ownercode = ownercode # instance attribute
        self.conents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1