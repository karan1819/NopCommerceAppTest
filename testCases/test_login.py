import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_Login:

    ## Here below Variables are hardcoded , therefore we need to create seperate file for them (.ini file needs to be created and utility file(for connection between .ini file and testcase file ))
    ## Copy below variables data into ini file
    #baseURL = "https://admin-demo.nopcommerce.com/"
    #username = "admin@yourstore.com"
    #password = "admin"

    ## Importing data from readProperties file
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    ## Logger from CustomLogger file
    logger = LogGen.loggen()

    ## To Group multiple Tests together sanity and regression group names have been used
    @pytest.mark.regression
    def test_homePageTitle(self, setup):   ## Setup because in conftest.py file contains driver information
        self.logger.info("********** TEST_001_Login **********")
        self.logger.info("********** Verifying Home Page Titlw **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        #self.driver.get("https://admin-demo.nopcommerce.com/")
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home Page Title Passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")  ## Capturing SS if tests failed
            self.driver.close()
            self.logger.error("********** Home Page Title Failed **********")
            assert False

    @pytest.mark.sanity  ## To Group multiple Tests together sanity and regression group names have been used
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********** Verifying Login Test **********")
        self.driver = setup
        #self.driver.get("https://admin-demo.nopcommerce.com/")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        tit = self.driver.title
        if tit == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
        #self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"Not SAME!!")
