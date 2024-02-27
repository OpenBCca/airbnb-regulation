from models.listing import Listing
from models.address import Address
from typing import List

class MockStore:
    def get_listings(self):
        self.store: List[Listing] = [
            Listing('1', address=Address(city='Vancouver'), licence_number='REG123'),
            Listing('2', address=Address(city='Vancouver'), licence_number='REG456'),
            Listing('3', address=Address(city='Vancouver'), licence_number='REG789')
        ]
        return self.store