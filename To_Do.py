# Variables (columns)
name = column1
priority = column2
tools = column3
location = column4
time = column5
materials = column6

# Add Task button, adds a row to the table using arguments as columns
def Add_Task(name, priority, details, tools, location, time, materials)
    %sql INSERT INTO 'to_do_list' (column1, column2, column3, column4, column5, column6) VALUES(name, priority, details, tools, location, time, materials)

# search function

# drop down list for sub categories

# search if to do item is already created

# add new row for materials and/or tools when inputing new task

# 