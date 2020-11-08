from scheduler import *

# Reading Week of EngSci 2T3

ddl = "2020, 11,"

NewHacks = Task("NewHacks", convert(ddl, "08, 11, 00"), 0.2, 600)

AER210_demo1 = Task("AER210_demo1", convert(ddl), 0, 33)
AER210_demo2 = Task("AER210_demo2", convert(ddl), 0, 28)
AER210_demo3 = Task("AER210_demo3", convert(ddl), 0, 20)
AER210_demo4 = Task("AER210_demo4", convert(ddl), 0, 20)

AER210_lec1 = Task("AER210_lec1", convert(ddl), 0.1, 45*1)
AER210_lec2 = Task("AER210_lec2", convert(ddl), 0.1, 35*1)
AER210_lec3 = Task("AER210_lec3", convert(ddl), 0.1, 20*1)
AER210_lec4 = Task("AER210_lec4", convert(ddl), 0.1, 30*1)
AER210_lec5 = Task("AER210_lec5", convert(ddl), 0.1, 30*1)
AER210_lec6 = Task("AER210_lec6", convert(ddl), 0.1, 30*1)
AER210_lec7 = Task("AER210_lec7", convert(ddl), 0.1, 30*1)



current_time = datetime.now()
test_available_time = [[current_time, convert(test_ddl)]]