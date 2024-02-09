class ListingStore:
    def __init__(self, source):
        if source == 'mock':
            self.store = self.get_items_from_mock_store()
        # can add more methods in future

    def get_items_from_mock_store(self):
        self.store = [
            {
                'listing_id': '1',
                'city': 'Vancouver',
                'registration_number': 'REG123'
            },
            {
                'listing_id': '2',
                'city': 'Vancouver',
                'registration_number': 'REG456'
            },
            {
                'listing_id': '3',
                'city': 'Vancouver',
                'registration_number': 'REG789'
            }
        ]
        return self.store