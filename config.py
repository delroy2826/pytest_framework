# Browser Configuration
implicit_wait = False
wait_time = 20
# Database Configuration
database_execute = False
host = "localhost"
database = None
user = 'root'
password = 'S01titude#'

# Ecommerce
url = "https://rahulshettyacademy.com/loginpagePractise/"

# API configuration
"""
If BASE_URL = None, HEADERS= None then arguments needs to be defined in testcases while creating object for the POM
Example 
test_userdata_api.py -> test_TC_1_API : 
user_data_api_page = UserDataApi("https://dummyapi.io/data/v1", {"app-id": "643fb1aea6fead45895bbf2c"})
"""
BASE_URL = "https://dummyapi.io/data/v1"
HEADERS = {"app-id": "643fb1aea6fead45895bbf2c"}
# BASE_URL = None
# HEADERS = None
