import json


def read_json_test_data(request) -> dict:
    with open(f'test_data/jsons/{request.node.originalname}.json', 'r') as f:
        data = json.load(f)
    return data
