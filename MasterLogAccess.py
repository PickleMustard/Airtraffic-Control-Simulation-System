import mysql.connector
import enum

#This file allows access to the Master Log Database
#Objects of this class will be able to interact in a limited capacity with the database

class Column_headers(enum.Enum):
	date = 1
	action_performed = 2
	additional_details = 3
	had_incident = 4
	plane_number = 5

class MasterLogAccess():
	
	def __init__(self):
		print("Initialiing")
		global MasterLog
		MasterLog = mysql.connector.connect(
			host="localhost",
			user="picklemustard",
			password="Purple14735#",
			database="Master_Log"
		)
		global MasterLogCursor
		MasterLogCursor = MasterLog.cursor()

		#*Created Table*
		#MasterLogCursor.execute("CREATE TABLE logs (date DATETIME PRIMARY KEY, action_performed VARCHAR(3000), additional_details VARCHAR(3000), had_incident BOOLEAN, aircraft_number INT)")	
		print("Showing Tables:")
		MasterLogCursor.execute("SHOW TABLES")
		for x in MasterLogCursor:
			print(x)

	#Adds a row with the given variables
	def add_Row(self, action_performed, additional_details, had_incident, aircraft_number):
		sql = "INSERT INTO logs (date, action_performed, additional_details, had_incident, aircraft_number) VALUES ( NOW(), %s, %s, %s, %s )"
		val = (action_performed, additional_details, had_incident, aircraft_number)
		MasterLogCursor.execute(sql, val)
		#sql = "INSERT INTO logs (date, action_performed, additional_details, had_incident, aircraft_number) VALUES (NOW(), 'Testing', 'Testing addition', 0, 1234)"

	#Deletes a row given a certain key
	#TODO: Input validation for all the Deletion
	def delete_Row(self, date_time):
		sql = "DELETE FROM logs WHERE date = %s"
		val = (date_time)
		MasterLogCursor.execute(sql, val)

	#Deletes a row given a certain key and action
	def delete_Row_Action_Perfomed(self, date_time, value_details):
		sql = "DELETE FROM logs WHERE date = %s AND action_perfomed = %s"
		val = (date_time, value_details)
		MasterLogCursor.execute(sql, val)

	#Deletes a row given a certain key and whether the log is detailing an incident
	def delete_Row_had_incident(self, date_time, had_incident):
		sql = "DELETE FROM logs WHERE date = %s AND had_incident = %b"
		val = (date_time, had_incident)
		MasterLogCursor.execute(sql, val)

	#Deletes a row given a certain key and aircraft number
	def delete_Row_aircraft_number(self, date_time, aircraft_number):
		sql = "DELETE FROM logs WHERE date = %s AND aircraft_number = %d"
		val = (date_time, aircraft_number)
		MasterLogCursor.execute(sql, val)

	#Updates a row or rows given a certain date and aircraft number with the given additional details
	#Nothing else should require updating as it will be set when entered in the database
	def update_Row_additional_details(self, date_time, additional_details, aircraft_number):
		sql = "UPDATE logs SET additional_details = %s WHERE date = %s AND aircraft_number = %d"
		val = (additional_details, date_time, aircraft_number)
		MasterLogCursor.execute(sql, val)

	#Does a general search through the table
	#Returns every row and column
	def general_search(self):
		sql = "SELECT * FROM logs"
		MasterLogCursor.execute(sql)
		return MasterLogCursor.fetchall()
	
	#Temporary Search Query for testing
	#Was created to test the display functionality
	def temporary_Info_List_Search(self):
		sql = "SELECT aircraft_number, action_performed FROM logs"
		MasterLogCursor.execute(sql)
		return MasterLogCursor.fetchall()

	#Searches for a specific item given a search value
	#Is given a specific column from the enum to determine the query
	def specific_search(self, column, search_value):
		if(column == Column_number.date):
			sql = "SELECT * FROM logs WHERE date = %s"
			val = (search_value)
			MasterLogCurosr.execute(sql, val)
			return MasterLogCursor.fetchall()
		elif(column == Column_number.action_performed):
			sql = "SELECT * FROM logs WHERE action_performed = %s"
			val = (search_value)
			MasterLogCurosr.execute(sql, val)
			return MasterLogCursor.fetchall()
		elif(column == Column_number.additional_details):
			sql = "SELECT * FROM logs WHERE additional_details = %s"
			val = (search_value)
			MasterLogCurosr.execute(sql, val)
			return MasterLogCursor.fetchall()
		elif(column == Column_number.had_incident):
			sql = "SELECT * FROM logs WHERE had_incident = %b"
			val = (search_value)
			MasterLogCurosr.execute(sql, val)
			return MasterLogCursor.fetchall()
		elif(column == Column_number.aircraft_number):
			sql = "SELECT * FROM logs WHERE aircraft_number = %d"
			val = (search_value)
			MasterLogCurosr.execute(sql, val)
			return MasterLogCursor.fetchall()
		else:
			return "Aint nothing with that value"
		