import json
from unittest.mock import Mock, patch

import pytest
from policy.services.business_licence_client import BusinessLicenceClient


@pytest.fixture
def client():
    return BusinessLicenceClient()


def mock_response(response_data=None):
    mock_response = Mock()
    if response_data:
        mock_response.data = json.dumps(response_data).encode("utf-8")
    else:
        mock_response.data = None
    return mock_response


@patch("policy.services.business_licence_client.urllib3.PoolManager")
@pytest.mark.parametrize(
    "licence_number, expected_status, expected_count",
    [
        ("0", [], 0),
        ("12-abcd", [], 0),
        ("20-247927", ["Issued"], 1),
        ("20-329038", ["Pending"], 1),
        ("20-254895", ["Cancelled"], 1),
        ("20-253595", ["Gone Out of Business"], 1),
        ("20-160574", ["Inactive", "Pending"], 2),
    ],
)
def test_get_licence_status_success(
    mock_pool_manager, client, licence_number, expected_count, expected_status
):
    mock_response_data = [
        {
            "total_count": expected_count,
            "results": [{"status": expected_status}],
        },
    ]
    mock_session = mock_pool_manager.return_value
    mock_session.request.return_value = mock_response(mock_response_data)
    actual_status = client.get_licence_status(licence_number)

    assert actual_status == expected_status
