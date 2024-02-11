import pytest
from report.src.listing_store.listing_store import ListingStore

def test_init():
    mock_store = ListingStore('mock')
    assert mock_store.store == mock_store.get_items_from_mock_store()

def test_get_items_from_mock_store():
    mock_store = ListingStore('mock')
    expected_store = [
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
    assert mock_store.get_items_from_mock_store() == expected_store