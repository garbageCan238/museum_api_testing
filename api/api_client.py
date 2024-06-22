import os
from api.routes import APIRoutes
from loguru import logger
from httpx import Client, Response, URL


class ApiClient(Client):
    def __init__(self, base_url):
        super().__init__(base_url=base_url)

    def request(self, method, url, **kwargs) -> Response:
        full_url = URL(f'{self.base_url}{url}', params=kwargs.get('params'))
        logger.info(f'Request: {method} {full_url}')
        response = super().request(method, url, **kwargs)
        logger.info(f'Response status code: {response.status_code}')
        return response


class MuseumApi(ApiClient):
    def __init__(self, base_url=os.getenv('BASE_URL')):
        super().__init__(base_url=base_url)

    def get_objects_api(self):
        logger.info(f'Getting all art objects')
        return self.get(APIRoutes.OBJECTS)

    def get_object_api(self, object_id: int):
        logger.info(f'Getting art object with id {object_id}')
        return self.get(f'{APIRoutes.OBJECTS}/{object_id}')

    def get_departments_api(self):
        logger.info(f'Getting departments list')
        return self.get(APIRoutes.DEPARTMENTS)

    def get_search_api(self, params: dict):
        logger.info(f'Getting search result with params: {params}')
        return self.get(f'{APIRoutes.SEARCH}', params=params)
