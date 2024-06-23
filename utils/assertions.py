from pydantic import BaseModel
from httpx import Response
from utils.file_utils import read_json_test_data


def validate_schema(response, model: type(BaseModel)):
    body = response.json()
    model.model_validate(body, strict=True)


def assert_status_code(response, expected_code):
    assert response.status_code == expected_code


def assert_response_body_fields(response: Response, json_filename: str):
    actual = response.json()
    expected = read_json_test_data(json_filename)
    for actual_key, expected_key in zip(actual.keys(), expected.keys()):
        assert actual_key == expected_key
        assert actual[actual_key] == expected[expected_key]
