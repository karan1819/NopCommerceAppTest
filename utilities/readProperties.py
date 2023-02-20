
import configparser

config = configparser.RawConfigParser()

## Read ini file
config.read(".\\Configurations\\config.ini")

## Getting Values from ini
class ReadConfig():

    @staticmethod   ## Using static method we can access the method directly using className without creating any object
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url
    def getUseremail():
        username = config.get('common info','username')
        return username
    def getPassword():
        password = config.get('common info','password')
        return password

