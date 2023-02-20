from selenium import webdriver
import pytest
from pageObjects.Addcustomerpage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import string
import random


@pytest.mark.sanity       ## To Group multiple Tests together sanity and regression group names have been used
class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_AddCustomer(self,setup):  ## Setup From conftest.py file
        self.logger.info("******* Test 003_Add_Customer *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**** Login Success *****")

        self.logger.info("**** Starting Add Customer Test")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("***** Providing Customer Info ******")

        ## Here email needs to be unique for each and every testcase, therefore random mails needs to be generated
        self.email = random_generator() + "@gmail.com"    ## Random_Generator function created below
        self.addcust.setEmail(self.email)
        self.addcust.setPass("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Karan")
        self.addcust.setLastName("Timmala")
        self.addcust.setDob("7/19/2001")
        self.addcust.setCompanyName("VK Comp")
        self.addcust.setAdminContent("This is for Testing purpose....")
        self.addcust.clickOnSave()

        self.logger.info("**** Saving Customer Info *****")

        self.logger.info("**** Add Customer Validation started *****")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        #print(self.msg)

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("Customer Added Successfully")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCust_scr.png")
            self.logger.error("Add Customer Failed")
            assert True == False
        self.driver.close()
        self.logger.info("****  Add Customer Test")


def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))




