import gspread
from google.oauth2.service_account import Credentials


# using caps here it's a global variable

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    (comments like this that describe what a function does should always be directly underneath the function name and within the function)
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas")
    print("Example: 10,20,30,40,50,60\n") # \n here creates new line in terminal, just tidies things up a bit

    # data will be returned as a string, so we call the input data_str
    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

    # below we're using the split() method to return the broken values as a list rather than as a string
    # values need to be in a list in order to be added to the G. sheet
    sales_data = data_str.split(",")
    print(sales_data)
# calling function:
get_sales_data()


# csv = comma-seperated values, file type that allows data to be saved in tablet format

