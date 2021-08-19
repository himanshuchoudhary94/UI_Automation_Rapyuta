from time import sleep
import pytest
from pageObjects.login_objects import LoginPage
from testData.login_data import LoginPageData
from utilities.base_class import BaseClass
from utilities.gwm_requests import GWMClient


class TestLogin(BaseClass):

    def test_check_correct_website_opened(self, getLoginData):
        """This function tests whether the website opened is correct or not"""

        assert self.driver.title == getLoginData["title"], "%s is incorrect Website" % self.driver.title

    def test_check_correct_login_password(self, getLoginData):
        """This function tests whether correct login password is passed for positive test scenario"""

        login_page = LoginPage(self.driver)
        login_page.enter_username(getLoginData['username'])
        login_page.enter_password(getLoginData['password'])
        login_page.click_login()
        sleep(10)
        # home_page = HomePage(self.driver)
        # assert home_page.items_menu_visibility(), "Unable to find to the sign in window"

    def test_check_payload_work(self, getLoginData):
        gwm_client = GWMClient()
        gwm_client.create_payload_work(pick=[3108227967439329], drop=1582209640687421)
        sleep(10)

    @pytest.fixture(params=LoginPageData.LOGIN_PAGE_DATA)
    def getLoginData(self, request):
        return request.param