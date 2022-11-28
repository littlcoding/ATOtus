import datetime
import pytest
import logging

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser to run tests")
    parser.addoption("--headless", action="store_true", help="browser to run tests")
    parser.addoption("--base_url", default="http://192.168.0.5:8081", help="browser to run tests")
    parser.addoption("--executor", action="store", default="192.168.0.5")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--videos", action="store_true")
    parser.addoption("--bv")

@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    #headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    # if browser == 'chrome':
    #     options = webdriver.ChromeOptions()
    #
    #     if headless:
    #         options.headless = True
    #
    #     driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
    # elif browser == 'firefox':
    #     driver = webdriver.Firefox()
    # elif browser == 'opera':
    #     driver = webdriver.Opera()
    # elif browser == 'safari':
    #     driver = webdriver.Safari()
    # else:

    caps = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
        }

    driver = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            desired_capabilities=caps
        )

    driver.base_url = base_url
    driver.get(base_url)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser:{}".format(browser, driver.caps))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
