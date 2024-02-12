import json

import urllib3
from models.address import Address
from models.listing import Listing
from urllib3.exceptions import HTTPError


class BusinessLicenceClient:
    BASE_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/business-licences/records"

    def __init__(self) -> None:
        self.session = urllib3.PoolManager()

    def _filter_by_licence_number(self, licence_number: str) -> dict:
        # Omit licence_number validity check since it should be checked during policy evaluation
        return {"where": f'licencenumber="{licence_number}"'}

    def _filter_by_short_term_rental_business(self) -> dict:
        return {"where": 'businesstype="Short-Term Rental"'}

    def _licence_status_query(self) -> dict:
        return {"select": "status"}

    def _make_request(self, fields: dict) -> dict:
        try:
            response = self.session.request(
                method="GET", url=self.BASE_URL, fields=fields
            )
            return json.loads(response.data)
        except HTTPError as e:
            print(f"Error fetching data: {e}")
            raise e

    def _process_licence_status_results(
        self, response_data: dict, licence_number: str
    ) -> str | list[str]:
        total_count = response_data["total_count"]
        results = response_data["results"]
        licence_status = [result["status"] for result in results]

        # Omit total_count == 0 case since the licence number should be checked during policy evaluation
        if total_count > 1:
            print(
                f"Received {total_count} counts of licence number with statuses: {licence_status}"
            )
        return licence_status

    def _merge_query_parameters(self, *parameters: dict) -> dict:
        merged_query_parameter = {}
        for parameter in parameters:
            for key, value in parameter.items():
                if key in merged_query_parameter:
                    merged_query_parameter[key] += f" and {value}"
                else:
                    merged_query_parameter[key] = value
        return merged_query_parameter

    def get_licence_status(self, licence_number: str) -> list[str]:
        fields = self._merge_query_parameters(
            self._filter_by_short_term_rental_business(),
            self._filter_by_licence_number(licence_number),
            self._licence_status_query(),
        )
        response_data = self._make_request(fields)

        return self._process_licence_status_results(response_data, licence_number)
