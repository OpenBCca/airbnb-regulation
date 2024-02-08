class Listing:
    """ Example listing: 105-2277 West 2nd Avenue, Vancouver, BC 
    with licence number 15-101054 and id 1234
    
    id: "1234"
    unit: "105"
    street_number: "2277"
    street: "West 2nd Avenue"
    city: "Vancouver"
    province: "BC"
    licence_number: "15-101054"
    """
    def __init__(self, **kwargs):
        mandatory_args = ["id", "street_number", "street", "city", "province", "licence_number"]
        missing_args = [arg for arg in mandatory_args if kwargs.get(arg) is None]
        if missing_args:
            raise ValueError(f"Missing argument(s): {', '.join(missing_args)}")
        
        self.id = kwargs.get("id")
        self.unit = kwargs.get("unit")
        self.street_number = kwargs.get("street_number")
        self.street = kwargs.get("street")
        self.city = kwargs.get("city")
        self.province = kwargs.get("province")
        self.licence_number = kwargs.get("licence_number")

    def print_listing(self):
        print(f"Listing address: {self.street_number}, {self.city}, {self.province}")

    