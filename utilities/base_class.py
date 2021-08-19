import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:
    def explicit_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))