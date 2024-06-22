from http import HTTPStatus

parameters = [
    ({'q': 'test', 'isHighlight': 'true'}, HTTPStatus.OK),
    ({'q': 'Painting', 'title': 'Song'}, HTTPStatus.OK),
    ({'q': 'Costume', 'dateBegin': 1870, 'dateEnd': 1960}, HTTPStatus.OK),
    ({'q': 'Diamond', 'geoLocation': 'Paris'}, HTTPStatus.OK),
    ({'q': 'test', 'isHighlight': 'true', 'geoLocation': 'Moscow'}, HTTPStatus.OK)]
