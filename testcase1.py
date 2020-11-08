from scheduler import*

test_ddl = "2020, 11, 08, 10, 00"
test_tasks = [Task("test1", convert(test_ddl), 0.5, 30)]


assignment1_ddl = "2020, 11, 08, 10, 00"
test_tasks.append(Task("test2", convert(test_ddl), 0.1, 120))

current_time = datetime.now()
test_available_time = [[current_time, convert(test_ddl)]]
schedule_dict = schedule(test_tasks, test_available_time)

for task_UUID, schedules in schedule_dict.items():
    print(UUID2Name[task_UUID], "is schedule between")
    for start_end in schedules:
        print("start:", str(start_end[0]))
        print("end  :", str(start_end[1]))