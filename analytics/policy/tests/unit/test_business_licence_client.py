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
    "licence_number, expected_status",
    [
        ("", []),
        (None, []),
        ("0", []),
        ("12-abcd", []),
        ("20-247927", ["Issued"]),
        ("20-329038", ["Pending"]),
        ("20-254895", ["Cancelled"]),
        ("20-253595", ["Gone Out of Business"]),
        ("20-160574", ["Pending", "Inactive"]),
    ],
)
def test_get_licence_status_success(
    mock_pool_manager, client, licence_number, expected_status
):
    mock_response_data = [
        {
            "total_count": len(expected_status),
            "results": [{"status": expected_status}],
        },
    ]
    mock_session = mock_pool_manager.return_value
    mock_session.request.return_value = mock_response(mock_response_data)
    actual_status = client.get_licence_status(licence_number)

    assert actual_status == expected_status
