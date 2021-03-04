import csv

with open('grants.csv','r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    #pull row1
    #transpose
    #print as html table

grants = open('grants.csv', 'r')
DictReader.grants() #may not be the best way to do this but seems like attaching keys would be a good idea, or is there a way to grab each row plus header?
grants1 = grants.iloc[1] #I know this is pandas not csv but grab row 1
grants1.t #I know this is pandas not csv but transpose and yes i know this is a dictionary so just format? not transpose?
#convert to html table
#repeat for subsequent rows
#print into html txt file
grants.close




********************************
Getting Individual Values in a List with Indexes

>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0]
'cat'

>>> spam[1]
'bat'

>>> spam[2]
'rat'

>>> spam[3]
'elephant' 
**************************************
Finding a Value in a List with the index Method

>>> spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']

>>> spam.index('Pooka')
1 