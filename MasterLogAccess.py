import mysql.connector
import enum

#What needs to be added:
#Using mysqldump to Backup data to Github and push it to people downloading repository
#Need another database that uses the departure time along with the plane number

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

	def add_Row(self, action_performed, additional_details, had_incident, aircraft_number):
		sql = "INSERT INTO logs (date, action_performed, additional_details, had_incident, aircraft_number) VALUES ( NOW(), %s, %s, %s, %s )"
		val = (action_performed, additional_details, had_incident, aircraft_number)
		MasterLogCursor.execute(sql, val)
		#sql = "INSERT INTO logs (date, action_performed, additional_details, had_incident, aircraft_number) VALUES (NOW(), 'Testing', 'Testing addition', 0, 1234)"

	def delete_Row(self, date_time):
		sql = "DELETE FROM logs WHERE date = %s"
		val = (date_time)
		MasterLogCursor.execute(sql, val)

	def delete_Row_Action_Perfomed(self, date_time, value_details):
		sql = "DELETE FROM logs WHERE date = %s AND action_perfomed = %s"
		val = (date_time, value_details)
		MasterLogCursor.execute(sql, val)

	def delete_Row_had_incident(self, date_time, had_incident):
		sql = "DELETE FROM logs WHERE date = %s AND had_incident = %b"
		val = (date_time, had_incident)
		MasterLogCursor.execute(sql, val)

	def delete_Row_aircraft_number(self, date_time, aircraft_number):
		sql = "DELETE FROM logs WHERE date = %s AND aircraft_number = %d"
		val = (date_time, value_details)
		MasterLogCursor.execute(sql, val)

	def update_Row_additional_details(self, date_time, additional_details, aircraft_number):
		sql = "UPDATE logs SET additional_details = %s WHERE date = %s AND aircraft_number = %d"
		val = (additional_details, date_time, aircraft_number)
		MasterLogCursor.execute(sql, val)

	def general_search(self):
		sql = "SELECT * FROM logs"
		MasterLogCursor.execute(sql)
		return MasterLogCursor.fetchall()

	def specific_search(self, column, search_value):
		if(column == Column_number.date):
			sql = "SELECT * FROM logs WHERE date = %s"
			val = (search_value)
			MasterLogCurosr.execute(sql, val)
		elif(column == Column_number.action_performed):
			sql = "SELECT * FROM logs WHERE action_performed = %s"
			val = (search_value)
			MasterLogCurosr.execute(sql, val)
		elif(column == Column_number.additional_details):
			sql = "SELECT * FROM logs WHERE additional_details = %s"
			val = (search_value)
			MasterLogCurosr.execute(sql, val)
		elif(column == Column_number.had_incident):
			sql = "SELECT * FROM logs WHERE had_incident = %b"
			val = (search_value)
			MasterLogCurosr.execute(sql, val)
		elif(column == Column_number.aircraft_number):
			sql = "SELECT * FROM logs WHERE aircraft_number = %d"
			val = (search_value)
			MasterLogCurosr.execute(sql, val)
		else:
			return "Aint nothing with that value"
		