# to interact with Google Spreadsheets
import gspread
# to authorize with the Google Drive API using OAuth 2.0
from oauth2client.service_account import ServiceAccountCredentials
# to print in a pretty format 
import pprint

# using creds to create a client to interact with the Google Drive API 
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a google sheet by name and open the first sheet
sheet = client.open("Interest Form (Responses)").sheet1

# Create PP object to print in a pretty list
pp = pprint.PrettyPrinter()

# Extract and print all the values
interests = sheet.get_all_records()     #Interest is a list of dictionaries where the key are the questions and the values are the answers

                                        #Example: 
                                        #   [{'What is your first name?' : 'Angelo',    |
                                        #   'Are you a big or little?' : 'Little',      |----- A first dictionary in the list 
                                        #   'Cooking/Baking' : 'Love'},                 |
                                        #   ...
                                        #   {'What is your first name?' : 'Bob',        |
                                        #   'Are you a big or little? : 'Little'        |------Second dictionary in the list
                                        #   'Cooking/Baking' : Like'}                   |


pp.pprint(interests)


#row = sheet.row_values(3)              #Gets the value of the 3rd row 
#col = sheet.col_values(3)              #Gets the value of the 3rd column
#cell = sheet.cell(2,3).value           #Gets the specific value at cell (2,3)