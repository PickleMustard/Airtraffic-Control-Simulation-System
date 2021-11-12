import MasterLogAccess
import time
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

query_result = Log_access.general_search()
for x in query_result:
	print(x)