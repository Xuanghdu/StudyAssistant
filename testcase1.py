from scheduler import*

task_dict = {"test1":["2020, 11, 08, 10, 00", 0.5, 30],
        "assignment1":["2020, 11, 08, 1, 00", 0.1, 300],
        "assignment2":["2020, 11, 09, 1, 00", 0.9, 120]}

task_list = []
for key in task_dict:
    t = task_dict[key]
    t[0] = convert(t[0])
    task_list.append(Task(key,*t) )    

current_time = datetime.now()
end_time = max(task_dict.values(),key = lambda x:x[0])[0]

task_available_time = [[current_time,  end_time]]


pretty_print(task_list, task_available_time)
