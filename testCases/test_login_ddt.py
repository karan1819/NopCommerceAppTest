import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_Login:

    ## Here below Variables are hardcoded , therefore we need to create seperate file for them (.ini file needs to be created and utility file(for connection between .ini file and testcase file ))
    ## Copy below variables data into ini file
    #baseURL = "https://admin-demo.nopcommerce.com/"
    #username = "admin@yourstore.com"
    #password = "admin"

    ## Importing data from readProperties file
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"

    ## Logger from CustomLogger file
    logger = LogGen.loggen()

    # @pytest.mark.sanity  ## To Group multiple Tests together sanity and regression group names have been used
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********** TEST_002_DDT_Login **********")
        self.logger.info("********** Verifying DDT TestLogin Test **********")
        self.driver = setup
        #self.driver.get("https://admin-demo.nopcommerce.com/")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        print(f"No.of Rows {self.rows}")

        lst_status=[]   ## EMpty list
        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("Failed!!")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("Failed!!")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT Test Passed....")
            assert True
            #self.driver.close()
        else:
            self.logger.info("Login DDT Test Failed!!")
            assert False
            #self.driver.close()


