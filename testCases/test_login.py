import pytest
from selenium import webdriver
from pageObjects.Loginpage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("********* Test_01_Login **********")
        self.logger.info("********* Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********* Home page title test is passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********* Home page title test is failed  **********")
            assert False


    def test_login(self,setup):
        self.logger.info("********* Verifying Login test  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title=="Dashboard / nopcommerce administration":
            assert True
            self.logger.info("********* Login test passed  **********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginTitle.png")
            self.driver.close()
            self.logger.error("********* Login test is failed  **********")
            assert False
