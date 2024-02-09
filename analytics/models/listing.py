from models.address import Address


class Listing:
    """Example listing in Vancouver
    with id 1234 and licence number 15-101054

    id: "1234"
    city: "Vancouver"
    licence_number: "15-101054"

    Attributes:
        id (str): The unique identifier for the listing.
        address (Address): The address of the listing.
        licence_number (str): The licence number associated with the listing.
    """

    def __init__(self, id: str, *, address: Address, licence_number: str = None):
        if not isinstance(address, Address):
            raise TypeError("address must be an instance of the Address class")

        self.id = id
        self.address = address
        self.licence_number = licence_number
