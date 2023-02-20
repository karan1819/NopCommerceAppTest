import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


## To RUn on different browsers also
#@pytest.fixture()
#def setup(browser):
#    if browser== "chrome":
#        driver = webdriver.Chrome()
#    elif browser== "Ie":
#        driver = webdriver.Firefox()
#    else:
#        driver = webdriver.Ie()
#    return driver

## To RUn on different browsers also
#def pytest_adoption(parser): ## This will get value from CLI /hooks
#    parser.adoption("--browser")

#@pytest.fixture()
#def browser(request):
#    return request.config.getoption("--browser")

## run in terminal with
# pytest -v -s testCases/test_login.py --browser Firefox

## To run tests in parallel browsers
# pytest -v -s -n=3 testCases/test_login.py --browser Firefox


#### PYTEST HTML REPORT ######

# Hook for Adding Environment info
def pytest_configure(config):
    config._metadata['Project Name'] = 'NOP Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'T.Karan'

# Hook to deleteModify Environment info
#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
#    metadata.pop("JAVA_HOME",None)
#    metadata.pop("Plugins",None)

## To generate html report in terminal type:
# pytest -v -s --html=Reports\report.html testCases/test_login.py