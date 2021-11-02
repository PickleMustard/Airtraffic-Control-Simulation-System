import mysql.connector
import enum

#What needs to be added:
#Create the database and tables initially
#Create add log query
#Create delete log query
#Create update log query
#Ask how table for showing works
#Create general selection query
#Create search query
MasterLog = mysql.connector.connect(
	host="localhost",
	user="picklemustard",
	password="Purple14735#",
	database="Master_Log"
)

class column_headers(enum.Enum):
	date = 1
	action_performed = 2
	additional_details = 3
	had_incident = 4
	plane_number = 5

MasterLogCursor = MasterLog.cursor()

#*Created Table*
#MasterLogCursor.execute("CREATE TABLE logs (date DATETIME PRIMARY KEY, action_performed VARCHAR(3000), additional_details VARCHAR(3000), had_incident BOOLEAN, aircraft_number INT)")

print("Showing Tables:")
MasterLogCursor.execute("SHOW TABLES")
for x in MasterLogCursor:
	print(x)
	
def add_Row(action_performed, additional_details, had_incident, aircraft_number):
	#do stuff
	
def delete_Row(column_number):
	#do stuff
	
def delete_Row_Specific(column_number, value_details):
	#do stuff

def update_Row(column_number, new_details):
	#do stuff

def update_Row_Specific(column_number, old_details, new_details):
	#do stuff
	
def general_search():
	#do stuff
	
def specific_search(column_number, search_value):
	#do stuff
