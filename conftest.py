import pytest

from selenium import webdriver

from src.Circle import Circle
from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from pages import Base_page



@pytest.fixture
def circle_1():
    return Circle(radius=4)

@pytest.fixture
def triangle_1():
    return Triangle(side_a=3, side_b=4, side_c=5)

@pytest.fixture
def square_1():
    return Square(side=5.5)

@pytest.fixture
def rectangle_1():
    return Rectangle(side_a=4, side_b=6)

def pytest_addoption(parser: object):
    parser.addoption(
        "--browser", default="chrome", help="browser to run tests"
    )
    parser.addoption(
        "--headless", action="store_true", help="browser to run tests"
    )
    parser.addoption(
        "--base_url", default="http://192.168.0.5:8081/", help="browser to run tests"
    )

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")

    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()

        if headless:
            options.headless = True

        _browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
    elif browser_name == 'firefox':
        _browser = webdriver.Firefox()
    elif browser_name == 'opera':
        _browser = webdriver.Opera()
    elif browser_name == 'safari':
        _browser = webdriver.Safari()

    _browser.base_url = base_url
    _browser.get(base_url)

    yield _browser

    _browser.close()
