"""

    """

import gspread
from google.oauth2.service_account import Credentials

from src.trck.models import gsh
import pandas as pd

class Vars :
    n = 'N'
    i = 'I'
    d = 'D'

v = Vars()

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(gsh.creds , scopes = scopes)
client = gspread.authorize(creds)

workbook = client.open_by_key(gsh.sheet_id)

##
sht = workbook.worksheet("Sheet1")

##
df = pd.DataFrame(sht.get_all_records())

##
df.columns

##
sht.update_cell(2 , 3 , '=B2-B4')

##

values = [["Name" , "Price" , "Quantity"] , ["Basketball" , 29.99 , 1] ,
        ["Jeans" , 39.99 , 4] , ["Soap" , 7.99 , 3] , ]

worksheet_list = map(lambda x : x.title , workbook.worksheets())
new_worksheet_name = "Values"

if new_worksheet_name in worksheet_list :
    sheet = workbook.worksheet(new_worksheet_name)
else :
    sheet = workbook.add_worksheet(new_worksheet_name , rows = 10 , cols = 10)

sheet.clear()

sheet.update(f"A1:C{len(values)}" , values)

sheet.update_cell(len(values) + 1 , 2 , "=sum(B2:B4)")
sheet.update_cell(len(values) + 1 , 3 , "=sum(C2:C4)")

sheet.format("A1:C1" ,
             {
                     "textFormat" : {
                             "bold" : True
                             }
                     })
