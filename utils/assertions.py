from pydantic import BaseModel

from models.art_objects import SearchResult


def validate_schema(response, model: type(BaseModel)):
    body = response.json()
    model.model_validate(body, strict=True)


def assert_status_code(response, expected_code):
    assert response.status_code == expected_code


def assert_response_body_fields(response, expected: BaseModel):
    actual = expected.model_validate(response.json())
    assert actual == expected
