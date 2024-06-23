from enum import Enum


class APIRoutes(str, Enum):
    OBJECTS = 'objects'
    DEPARTMENTS = 'departments'
    SEARCH = 'search'

    def __str__(self) -> str:
        return self.value
