import pytest
from http import HTTPStatus
from models.art_objects import ArtObject, SearchResult
from pydantic import ValidationError
from loguru import logger


def test_get_art_object(api_client):
    object_id = 1
    response = api_client.get_object_api(object_id)
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    try:
        ArtObject.model_validate(data, strict=True)
    except ValidationError:
        logger.error('Validation error')
        pytest.fail('Data validation error')


def test_get_nonexistent_art_object(api_client):
    object_id = -1
    response = api_client.get_object_api(object_id)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_search_result(api_client):
    params = {'q': 'sunflower'}
    response = api_client.get_search_api(params=params)
    data = response.json()
    try:
        SearchResult.model_validate(data, strict=True)
    except ValidationError:
        logger.error('Validation error')
        pytest.fail('Data validation error')
