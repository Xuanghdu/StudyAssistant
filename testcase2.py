from scheduler import *

# Reading Week of EngSci 2T3

ddl = "2020, 11,"

tasks = []
tasks.append(Task("NewHacks", convert(ddl+"08, 11, 00"), 0.2, 60))
tasks.append(Task("AER210_demo2", convert(ddl+"10, 00, 00"), 0, 28))
tasks.append(Task("AER210_demo1", convert(ddl+"09, 00, 00"), 0, 33))
tasks.append(Task("AER210_demo3", convert(ddl+"11, 00, 00"), 0, 20))
tasks.append(Task("AER210_demo4", convert(ddl+"12, 00, 00"), 0, 2000))
tasks.append(Task("AER210_lec1", convert(ddl+"09, 00, 00"), 0.1, 45*1))
tasks.append(Task("AER210_lec2", convert(ddl+"10, 00, 00"), 0.1, 35*1))
tasks.append(Task("AER210_lec3", convert(ddl+"11, 00, 00"), 0.1, 20*1))
tasks.append(Task("AER210_lec4", convert(ddl+"12, 00, 00"), 0.1, 30*1))
tasks.append(Task("AER210_lec5", convert(ddl+"13, 00, 00"), 0.1, 30*1))
tasks.append(Task("AER210_lec6", convert(ddl+"14, 00, 00"), 0.1, 30*1))
tasks.append(Task("AER210_lec7", convert(ddl+"15, 00, 00"), 0.1, 30*1))

current_time = datetime.now()
test_available_time = [[current_time, last_ddl(tasks)]]

occupied_time = [convert(ddl+"7,23,00"), convert(ddl+"8,7,00")]
test_available_time = add_occupied_time(occupied_time, test_available_time, frequency=timedelta(days=1))

pretty_print(tasks, test_available_time)
