from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
class AddCustomer:

    ## Add Customer Page
    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    #lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    #lnkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    btnAddnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a/i"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_id = "DateOfBirth"
    txtCompanyName_id = "Company"
    txtcustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    drpmgrOfVendor_id = "VendorId"
    txtAdminContent_id = "AdminComment"
    btnSave_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"
    lstitemAdminitrators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lsttitemRegistered_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    lstitemGuests_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitemVendor_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    lstitemforum_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)
    def setPass(self,password):
        self.driver.find_element(By.ID,self.txtPassword_id).send_keys(password)
    def setFirstName(self,fn):
        self.driver.find_element(By.ID,self.txtFirstName_id).send_keys(fn)
    def setLastName(self,ln):
        self.driver.find_element(By.ID,self.txtLastName_id).send_keys(ln)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lsttitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemAdminitrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role=='Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lsttitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.ID,self.drpmgrOfVendor_id))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setDob(self, dob):
        self.driver.find_element(By.ID,self.txtDob_id).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.ID,self.txtCompanyName_id).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.ID,self.txtAdminContent_id).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()

