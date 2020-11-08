from scheduler import *

test_ddl = "2020, 11, 08, 10, 00"
test_tasks = [Task("test1", convert(test_ddl), 0.5, 30)]
current_time = datetime.now()
test_available_time = [[current_time, convert(test_ddl)]]