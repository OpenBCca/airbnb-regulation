import pytest
from unittest.mock import MagicMock
from policy.services.registration_number_policies import RegistrationNumberPolicies

@pytest.fixture
def mock_http_response_200():
    response_mock = MagicMock()
    response_mock.status = 200
    response_mock.data = '{"total_count": 1}'
    return response_mock

@pytest.fixture
def mock_http_no_response():
    response_mock = MagicMock()
    response_mock.status = 200
    response_mock.data = '{"total_count": 0}'
    return response_mock

def test_valid_pattern():
    registration_number = "24-160188"
    registration_number_policies = RegistrationNumberPolicies(
        registration_number
    )
    assert registration_number_policies.valid_pattern() is True

def test_invalid_pattern():
    registration_numbers = [
        "24160188",
        "24-160a88",
        "24-1601883",
        "24-1601a8",
        "124-160188",
        "q4-160188",
        "4-160188",  
    ]
    for registration_number in registration_numbers:
        registration_number_policies = RegistrationNumberPolicies(
            registration_number
        )
        assert registration_number_policies.valid_pattern() is False

def test_valid_registration_number(mock_http_response_200):
    registration_number = "24-160188"
    registration_number_policies = RegistrationNumberPolicies(
        registration_number
    )
    registration_number_policies.session.request = MagicMock(
        return_value=mock_http_response_200
    )
    assert registration_number_policies.valid_registration_number() is True

def test_invalid_registration_number(mock_http_no_response):
    registration_number = "26-160188"
    registration_number_policies = RegistrationNumberPolicies(
        registration_number
    )
    registration_number_policies.session.request = MagicMock(
        return_value=mock_http_no_response
    )
    assert registration_number_policies.valid_registration_number() is False
