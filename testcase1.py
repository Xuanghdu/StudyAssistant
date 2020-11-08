from scheduler import*


task_dict = {"test1":["2020, 11, 08, 1, 00", 0.9, 60],
        "assignment2":["2020, 11, 08, 11, 00", 0.1, 310],
        "assignment1":["2020, 11, 08, 12, 00", 0.9, 300]
        }

task_list = []
for key in task_dict:
    t = task_dict[key]
    t[0] = convert(t[0])
    task_list.append(Task(key,*t))    

current_time = convert("2020, 11, 08, 0, 00")
end_time = max(task_dict.values(),key = lambda x:x[0])[0]

occupied_time = [convert("2020, 11, 08, 2, 00"),convert("2020, 11, 08, 3, 00")]
task_available_time = [[current_time,  end_time]]
task_available_time = add_occupied_time(occupied_time, task_available_time, frequency=timedelta(days=1))

pretty_print(task_list, task_available_time)
