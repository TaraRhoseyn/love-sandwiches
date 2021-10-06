import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Gets data from users in the terminal
    Splits that data to remove commas
    Passes data to sales_data if validate_data function is True
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas")
        print("Example: 10,20,30,40,50,60\n") 

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print('Data is valid')
            break # while loop is stopped if data is valid
    return sales_data        


def validate_data(values):
    """
    Converts user string values into inters.
    Raises ValueError if not exactly 5 values are entered
    returns True if try passes and False if ValueError called
    """
    try:
        [int(value) for value in values] # a list comprehension
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False
    return True

def update_worksheet(data, worksheet):
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stocks to calculate surplus stock
    Stock - sales = surplus
    """
    print("Calculating surplus data...")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1] # slicing last item from the list, so the final row
    
    surplus_data = []
    for stock, sales, in zip(stock_row, sales_row):
        """
        Iterating through stock_row & sales_row lists
        To calculate surplus
        """
        surplus = int(stock) - sales
        surplus_data.append(surplus)

def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")

print('Welcome to Love Sandwiches Data Automation')
main()