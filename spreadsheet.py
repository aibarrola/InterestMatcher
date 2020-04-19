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
interests = sheet.get_all_records()

# pp.pprint(interests)