import numpy as np  #for sql magic-- dont think this was correct and even if it was should be jupyter only?
import pandas as pd  #for dataframe read and export

pp_path = c/Desktop/DR15/Dow** 
sh_path = c/Desktop/DR15/Sel**
fe_path = c/Desktop/DR15/Fil**

df_p = pd.read_csv(pp_path)  ???#something seems wrong here
df_s = pd.read_csv(sh_path)
df_f = pd.read_csv(fe_path)

df_p.read_csv(pp_path)  
%%sql
    SELECT SUM('sales tax', 'gross')
    FROM paypal
    WHERE paypal.'sales tax' > 0 
???#store as variables pp_tax_fl pp_gross_fl


df_s.read_csv(sh_path)
df_f.read_csv(fe_path)

%%sql
    SELECT SUM('gross sales')
    FROM seller_hub
???#store as sh_gross
    
%%sql
    SELECT *
    FROM seller_hub
    JOIN file_exchange
        ON seller_hub.'Sales Record Number' = file_exchange.'Sales Record Number'  #sales record # in stead of item id should eliminate the need to clean the multiple item purchases
    
    SELECT *
    FROM seller_hub
    WHERE seller_hub.'Buyer State' = 'FL' OR 'Florida'

    SELECT SUM('sales tax', 'gross sales')
    FROM seller_hub
    WHERE Gain > 0
???#store as sh_tax_fl sh_gross_fl
    
???#input bike sales variables******* store as bs_tax_fl bs_gross_fl***** may need more here for bikes over 5k etc

tax_collected = pp_tax_fl + sh_tax_fl + bs_tax_fl

taxable_amount = pp_gross_fl + sh_gross_fl + bs_gross_fl

gross = sh_gross + pp_gross_fl + bs_gross_fl

exempt_sales = gross - taxable_amount

discretionary = (taxable_amount * .01) + #bike surtax

tax_calculated = (taxable_amount * .06) + discretionary

if tax_calculated > tax_collected
    total_due = tax_calculated
else:
    total_due = tax_collected

collection_allowance = total_due *.025 

if collection_allowance < 30
    less_collection_allowance = collection_allowance
else:
    less_collection_allowance = 30

amount_due = total_due - collection_allowance
#15a & 15c


print('1. Gross Sales:' + gross)
print('2. Exempt Sales:', exempt_sales)
print('3. Taxable Amount:', taxable_amount)
print('4. Tax Collected:', total_due)     
print('5. Total Amount of Tax Collected:', total_due)    
print('6. Less Lawful Deductions:', 'na')
print('7. Total Tax Due:', total_due)
print('8. Less Est Tax Pd/ DOR Cr Memo:', 'If you have a credit use it here. It will change variables #10 and #14.')
print('9. Plus Est Tax Due Current Month:', 'na')
print('10. Amount Due:', total_due, 'Will change if credit is used')
print('11. Less Collection Allowance:', less_collection_allowance)
print('12. Plus Penalty:', 'na')
print('13. Plus Interest:', 'na')
print('14. Amount Due with Return:', amount_due)
print('15(a). Exempt Amount of Items Over $5,000 (included in Column 3):', 'Did you sell any bikes over $5,000?')
print('15 (b). Other Taxable Amounts NOT  subject to Surtax (included in Column 3):', 'na')
print('15 c). Amounts Subject to Surtax at a Rate Different Than Your County Surtax Rate (included in Column 3):', )    ???#dont forget this
print('15 (d). Total Amount of Discretionary Sales Surtax Collected (included in Column 4):', discretionary)































*******************************************************************************************
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

***************************************************************************************************
# example for searching excell sheet. does it work for this aplication?

import numpy as np
import pandas as pd

excel_file = 'Pandas_Workbook.xlsx'
df = pd.read_excel(excel_file)
print(df)

print(df['Name'].where(df['Occupation'] == 'Programmer'))
programmers = df['Name'].where(df['Occupation'] == 'Programmer')
print(programmers.dropna())

excel_files = ['Pandas_Workbook.xlsx','Pandas_Workbook_copy.xlsx','Pandas_Workbook_copy_2.xlsx']

for individual_excel_file in excel_files:
    df = pd.read_excel(individual_excel_file)
    programmers = df['Name'].where(df['Occupation'] == 'Programmer').dropna()
    print("File Name" + individual_excel_file)
    print(programmers)

    *********************************************************************************
Loading a CSV into a table
You've done a great job so far at inserting data into tables! You're now going to learn how to load the contents of a CSV file into a table.

One way to do that would be to read a CSV file line by line, create a dictionary from each line, and then use insert(), like you did in the previous exercise.

But there is a faster way using pandas. You can read a CSV file into a DataFrame using the read_csv() function (this function should be familiar to you, but you can run help(pd.read_csv) in the console to refresh your memory!). Then, you can call the .to_sql() method on the DataFrame to load it into a SQL table in a database. The columns of the DataFrame should match the columns of the SQL table.

.to_sql() has many parameters, but in this exercise we will use the following:

name is the name of the SQL table (as a string).
con is the connection to the database that you will use to upload the data.
if_exists specifies how to behave if the table already exists in the database; possible values are "fail", "replace", and "append".
index (True or False) specifies whether to write the DataFrame's index as a column.
In this exercise, you will upload the data contained in the census.csv file into an existing table "census". The connection to the database has already been created for you.
***************************************************************************************
import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')