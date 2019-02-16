import json
from fixture.application import Application
import pytest
import os.path


@pytest.fixture()  # (scope = "session")
def app(request):
    browser = request.config.getoption("--browser")
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target.json"))
    with open(config_file) as f:
        target = json.load(f)
    fixture = Application(browser=browser, base_url=target['baseUrl'], language=target['language'])
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target.json", action="store", default="target.json")
