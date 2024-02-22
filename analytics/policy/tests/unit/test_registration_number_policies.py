import pytest
from policy.policies.registration_number_policies import RegistrationNumberPolicies

def test_valid_pattern():
    registration_number = "23-160188"
    registration_number_policies = RegistrationNumberPolicies(
        registration_number
    )
    assert registration_number_policies.valid_registration_number_policy() is True

def test_invalid_pattern():
    registration_numbers = [
        "24160188",
        "24-160a88",
        "24-1601883",
        "24-1601a8",
        "124-160188",
        "q4-160188",
        "4-160188",
        "123",
        "",
        None
    ]
    for registration_number in registration_numbers:
        registration_number_policies = RegistrationNumberPolicies(
            registration_number
        )
        assert registration_number_policies.valid_registration_number_policy() is False

def test_unique_registration_number_policy():
    registration_number = "24-160188"
    registration_number_policies = RegistrationNumberPolicies(registration_number) 
    assert registration_number_policies.unique_registration_number_policy() is True # (["Issued"], 1)

    registration_number = "20-160574"
    registration_number_policies = RegistrationNumberPolicies(registration_number) 
    assert registration_number_policies.unique_registration_number_policy() is False # (["Pending", "Inactive"], 1)

    registration_number = ""
    registration_number_policies = RegistrationNumberPolicies(registration_number)
    assert registration_number_policies.unique_registration_number_policy() is False # (["Issued", "Issued"], 2)

def test_existed_registration_number_policy():

    registration_number = "24-160188"
    registration_number_policies = RegistrationNumberPolicies(registration_number)
    assert registration_number_policies.existed_registration_number_policy() is True

    # assert registration_number_policies.existed_registration_number_policy() is False

    # assert registration_number_policies.existed_registration_number_policy() is False

