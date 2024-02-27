import pytest
from models.listing import Listing
from models.address import Address
from report.src.listing_store.listing_store import MockStore

def test_get_listings():
    mock_store = MockStore()
    listings = mock_store.get_listings()

    assert len(listings) == 3  # Check if there are 3 listings

    # Check if all listings are instances of Listing
    for listing in listings:
        assert isinstance(listing, Listing)

    # Check the details of the first listing
    first_listing = listings[0]
    assert first_listing.id == '1'
    assert first_listing.licence_number == 'REG123'
    assert isinstance(first_listing.address, Address)
    assert first_listing.address.city == 'Vancouver'