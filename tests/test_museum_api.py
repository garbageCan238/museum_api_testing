import pytest
from http import HTTPStatus
from models.art_objects import ArtObject, SearchResult, ArtObjects
from test_data.search_parameters import parameters
from utils.assertions import validate_schema, assert_status_code, assert_response_body_fields


def test_get_all_art_objects(api_client):
    response = api_client.get_objects_api()
    assert_status_code(response, HTTPStatus.OK)
    response.json()
    validate_schema(response, ArtObjects)


def test_get_art_object(api_client):
    object_id = 1
    response = api_client.get_object_api(object_id)
    assert_status_code(response, HTTPStatus.OK)
    validate_schema(response, ArtObject)


def test_get_nonexistent_art_object(api_client, request):
    object_id = -1
    response = api_client.get_object_api(object_id)
    assert_status_code(response, HTTPStatus.NOT_FOUND)
    assert_response_body_fields(response, request)


def test_get_search_result(api_client):
    params = {'q': 'sunflower'}
    response = api_client.get_search_api(params=params)
    assert_status_code(response, HTTPStatus.OK)
    validate_schema(response, SearchResult)


def test_get_search_result_with_no_query(api_client):
    params = {'departmentId': 1}
    response = api_client.get_search_api(params)
    assert_status_code(response, HTTPStatus.BAD_GATEWAY)


def test_get_search_result_with_future_date(api_client, request):
    params = {'q': ' ', 'dateBegin': 2400, 'dateEnd': 3000}
    response = api_client.get_search_api(params)
    assert_status_code(response, HTTPStatus.OK)
    validate_schema(response, SearchResult)
    assert_response_body_fields(response, request)


@pytest.mark.parametrize("params, expected_status_code", parameters)
def test_get_search_with_filters(api_client, params, expected_status_code):
    response = api_client.get_search_api(params)
    assert_status_code(response, expected_status_code)
    validate_schema(response, SearchResult)
