from pprint import pprint
import pytest
from selenium import webdriver
from utilities.BmpProxy import ProxyManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


def bmp_proxy():
    proxy = ProxyManager()
    bmp_server = proxy.start_server()
    bmp_client = proxy.start_client()
    bmp_client.new_har("payload_test")
    print(bmp_client.proxy)
    return bmp_client, bmp_server


@pytest.fixture(scope='class')
def setup(request):
    # browser = request.config.getoption('browser')
    # if browser == 'chrome':
    #     driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe",chrome_options=options)
    # elif browser == 'edge':
    #     driver = webdriver.edge(executable_path="drivers/msedgedriver.exe")
    options = webdriver.ChromeOptions()
    bmp_client, bmp_server = bmp_proxy()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--proxy-server={}".format(bmp_client.proxy))
    driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe", options=options)
    driver.get("https://himanshutrail11-amr-ui-kqdbp.ep-r.io/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    request.cls.webdriver = webdriver
    yield
    pprint(bmp_client.har)
    bmp_server.stop()
    driver.close()

