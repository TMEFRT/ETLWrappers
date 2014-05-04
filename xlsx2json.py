import xlrd
from collections import OrderedDict
import simplejson as json


FILE_LOC='/Users/aa/'

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook(FILE_LOC + 'wm_items.xlsx')
sh = wb.sheet_by_index(0)




# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):

    # defining cart as a dictionary type

# List to hold dictionaries
    cart_list = []
    cart = OrderedDict()

    row_values = sh.row_values(rownum)

    file_name=FILE_LOC + str(row_values[0]) + '.json'

    for i in range(0,len(row_values)):

        cart[sh.row_values(0)[i]] = row_values[i]

    cart_list.append(cart)
 
    # Serialize the list of dicts to JSON
    j = json.dumps(cart_list)

    # Write to file
    with open(file_name, 'w') as f:
        f.write(j)
