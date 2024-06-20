import os
import datetime
import pytest
from loguru import logger
from api.api_client import MuseumApi
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def configure_logging():
    log_filename = f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    logger.remove()
    logger.add(f"logs/{log_filename}", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO")


def pytest_runtest_logreport(report):
    if report.when == 'call':
        test_name = report.nodeid.split("::")[-1]
        if report.passed:
            logger.info(f'Test passed: {test_name}')
        elif report.failed:
            logger.error(f'Test failed: {test_name}')
        elif report.skipped:
            logger.info(f'Test skipped: {test_name}')


@pytest.fixture(scope="module")
def api_client():
    load_dotenv(dotenv_path=".env")
    return MuseumApi(os.getenv('BASE_URL'))


