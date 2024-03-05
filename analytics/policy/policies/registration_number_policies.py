import re
import json
from policy.services.business_licence_client import BusinessLicenceClient

class RegistrationNumberPolicies:
    def __init__(self, registration_number):
        self.registration_number = registration_number

    def valid_registration_number_policy(self):
        valid_registration_pattern = re.compile(r'^[0-9]{2}-[0-9]{6}$')
        START_YEAR = 13
        END_YEAR = 24

        if self.registration_number is None or self.registration_number == "":
            return False

        if valid_registration_pattern.match(self.registration_number):
            year = self.registration_number[0:2]
            if int(year) > END_YEAR or int(year) < START_YEAR:
                return False
            else:
                return True
        else:
            return False

    def unique_registration_number_policy(self):
        business_licences = BusinessLicenceClient()
        licence_status = business_licences.get_licence_status(
            self.registration_number
        )
        total_count = len(licence_status)
        if total_count == 1:
            return True
        else:
            return False

    def existed_registration_number_policy(self):
        business_licences = BusinessLicenceClient()
        licences_status = business_licences.get_licence_status(
            self.registration_number
        )
        total_count = len(licences_status)
        if total_count > 0:
            return True
        else:
            return False
