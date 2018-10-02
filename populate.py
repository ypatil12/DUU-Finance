from faker import Faker
import random
import csv
import xlwt

# Initialize faker and workbook of sheet
fakegen = Faker()
wb = xlwt.Workbook()
ws = wb.add_sheet("Data Set", cell_overwrite_ok = True)
# List of DUU committees
committees = [
'Campus Concerts', 'Coffehouse', 'Devops','Downtown Duke', 'Broadcasting','Freewater Presentations',
'Freewater Productions','Jazz','LDOC', 'Marketing','Speakers','Special Events','Small Town Records'
]

# Ramdomly generated committee
def get_committee():
    return random.choice(committees)

# Write headers for speadsheet
ws.write(0,0,"Committe")
ws.write(0,1,"Date")
ws.write(0,2,"Line Item")
ws.write(0,3,"Cost")

# Generate fake data
def generate_data(x=100):

    for entry in range(x):
        ws.write(entry+1, 0, get_committee())
        ws.write(entry+1, 1, fakegen.date_this_year())
        # Item/Service not available, just used bs keywords
        ws.write(entry+1, 2, fakegen.bs().split()[0])
        ws.write(entry+1, 3, random.randint(25,1000))

generate_data(100)
wb.save("data.xls")
