import os
import datetime
import time

import pytest
from loguru import logger
from api.api_client import MuseumApi
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def configure_logging():
    log_filename = f'log_{time.strftime("%Y-%m-%d_%H-%M-%S")}.log'
    logger.remove()
    logger.add(f'logs/{log_filename}', format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}', level='DEBUG')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    test_name = report.nodeid.split('::')[-1]
    if report.when == 'call' and report.passed:
        logger.info(f'Test passed: {test_name}')
    elif report.skipped:
        logger.info(f'Test skipped: {test_name}')
    if report.when == 'call' and report.failed:
        if call.excinfo.type == AssertionError:
            logger.error(f'Test failed: {item.name} - {call.excinfo.value}')
        else:
            logger.error(f'Test raised an exception: {item.name} - {call.excinfo.value}')


@pytest.fixture(scope='module')
def api_client():
    load_dotenv(dotenv_path='.env')
    client = MuseumApi(os.getenv('BASE_URL'))
    logger.debug('API client created')
    return client
