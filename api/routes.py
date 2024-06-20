from enum import Enum


class APIRoutes(str, Enum):
    OBJECTS = '/public/collection/v1/objects'
    DEPARTMENTS = '/public/collection/v1/departments'
    SEARCH = '/public/collection/v1/search'

    def __str__(self) -> str:
        return self.value
