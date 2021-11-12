import MasterLogAccess
import time

#Temporary class to test the implementation of database functionality
class TestingDatabases():
	
	#Upon its definition, adds some test values to the database
	def __init__(self):
		global Log_access
		Log_access = MasterLogAccess.MasterLogAccess()
		Log_access.add_Row("Test Entry", "This is an entry to test the table insertion method", 0, 1234)
		time.sleep(1)
		Log_access.add_Row("Test Entry", "This is an entry to test the table insertion method", 0, 1235)
		time.sleep(1)
		Log_access.add_Row("Test Entry", "This is an entry to test the table insertion method", 0, 1236)
		time.sleep(1)
		Log_access.add_Row("Test Entry", "This is an entry to test the table insertion method", 1, 1237)
		time.sleep(1)
		Log_access.add_Row("Test Entry", "This is an entry to test the table insertion method", 1, 1238)
		time.sleep(1)
		Log_access.add_Row("Test Entry", "This is an entry to test the table insertion method", 1, 1239)
		time.sleep(1)
		Log_access.add_Row("Test Entry", "This is an entry to test the table insertion method", 0, 1230)

	#Calls the general search method of the Master Log Database Access
	#Then prints the results of the query
	def gen_search():
		query_result = Log_access.general_search()
		for x in query_result:
			print(x)