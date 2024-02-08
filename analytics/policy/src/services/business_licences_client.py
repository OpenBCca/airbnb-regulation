import json
from typing import Dict

import urllib3
from listing import Listing
from src.utils.dict_utils import merge_dicts


class BusinessLicencesClient:
    BASE_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/business-licences/records"

    def __init__(self) -> None:
        self.session = urllib3.PoolManager()

    def get_listing_by_address(self, listing: Listing) -> Dict[str, str]:
        where_clause_parts = []
        for key, value in listing.__dict__.items():
            # Change street_number to house to match query parameter
            if key == "street_number":
                key = "house"
            if value != "":
                where_clause_parts.append(f'{key}="{value}"')

        where_clause = " and ".join(where_clause_parts)

        if where_clause:
            return {"where": where_clause}
        else:
            raise ValueError("No valid listing members provided")

    def get_listing_by_licence_number(self, listing: Listing) -> Dict[str, str]:
        where_clause = f'licencenumber="{listing.licence_number}"'
        return {"where": where_clause}

    def select_year(self, year: str) -> Dict[str, str]:
        return {"refine": f"folderyear:{year}"}

    def get_licence_status(self) -> Dict[str, str]:
        return {"select": "status"}

    def get_licence_number(self) -> Dict[str, str]:
        return {"select": "licencenumber"}

    def get_listing_licence_status(self, listing: Listing) -> str:
        response_fields = merge_dicts(
            self.get_listing_by_address(listing), self.get_licence_status()
        )
        response = self.session.request("GET", self.BASE_URL, fields=response_fields)
        data = response.data
        return json.loads(data)

    def get_listing_licence_number(self, listing: Listing) -> str:
        response_fields = merge_dicts(
            self.get_listing_by_address(listing), self.get_licence_number()
        )
        response = self.session.request("GET", self.BASE_URL, fields=response_fields)
        data = response.data
        return json.loads(data)


if __name__ == "__main__":
    example_listing = Listing(
        id="",
        unit="",
        street_number="",
        street="",
        city="Vancouver",
        licence_number="23-158599",
        province="BC",
    )
    example_listing.print_listing()
    business_licences = BusinessLicencesClient()
    print(business_licences.get_listing_licence_status(example_listing))
    print(business_licences.get_listing_licence_number(example_listing))
