import re
import json
import urllib3

class RegistrationNumberPolicies:
    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.session = urllib3.PoolManager()

    def valid_pattern(self):
        valid_registration_pattern = re.compile(r'^[0-9]{2}-[0-9]{6}$')

        if valid_registration_pattern.match(self.registration_number):
            return True
        else:
            return False

    def valid_registration_number(self):
        facet_name = "licencenumber"
        limit_value = 20
        OPEN_DATA_VANCOUVER_URL = (
            "https://opendata.vancouver.ca/"
            "api/explore/v2.1/catalog/datasets/"
            "business-licences/records?"
            f"limit={limit_value}&"
            f"refine={facet_name}%3A{self.registration_number}"
        )
        response = self.session.request(
                method="GET", url=OPEN_DATA_VANCOUVER_URL
            )

        if response.status == 200:
            response = json.loads(response.data)
            if response['total_count'] > 0:
                return True
            else:
                return False
        else:
            return False
