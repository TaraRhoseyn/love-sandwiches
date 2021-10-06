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
    # below we're using the split() method to return the broken values as a list rather than as a string
    # values need to be in a list in order to be added to the G. sheet
    sales_data = data_str.split(",")
    validate_data(sales_data)

# parameter = values
def validate_data(values):
    """
    Inside the true, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        # len() method means length
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    # 'e' is standard python shorthand for error
    # we're data the data from the inputted data
    # and putting it into the variable 'e'
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")

    print(values)

# calling function:
get_sales_data()


# csv = comma-seperated values, file type that allows data to be saved in tablet format

"""
Data type of anything inserted in the terminal by the user
is always a string. We need to convert data to ints
Can't do maths with strings.
"""

"""
in the terminal, open python shell
by typing "python3", shell will 
appear with >>>

"""