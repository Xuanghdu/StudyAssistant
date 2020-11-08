from datetime import datetime, timedelta

class Task():
    """
    task
    """

    __slots__ = 'UUID', 'name', 'ddl', 'weight', 'duration', 'cut'

    def __init__(self, name, ddl, weight, duration):
        """
        Parameters:
        ddl (datetime) : year, month, day, hour, minute
        weight (float) : [0, 1]
        duration (int) : in minute
        """
        self.name = name
        self.ddl = ddl
        self.weight = weight
        self.duration = timedelta(minutes=duration)

def convert(ddl):
    ddl = ddl.split(',')
    return datetime(int(ddl[0]), int(ddl[1]), int(ddl[2]), int(ddl[3]), int(ddl[4]))

def eval_priority(start_time, task):
    ddl_pressure = 1/((start_time + task.duration - task.ddl).seconds/60)
    # negative???
    return task.weight * ddl_pressure

def schedule(tasks, available_time):
    """([Tasks], [[datetime,datetime]]) -> {Task:[[datetime,datetime]]}
    Parameters:
    tasks:         : list of tasks
    available_time : two-dimensional array of [[begin,end]]
    Return:
    schedule_dict  : dict of task to two-dimensional array of [[begin,end]]
    """
    schedule_dict = {}
    for task in tasks:
        if task.ddl < datetime.now():
            print("{} is overdue\n".format(task.name))
            tasks.remove(task)
    for timeslot in available_time:
        priority = []
        start_time = timeslot[0]
        timeslot_duration = timeslot[1] - timeslot[0]
        while timeslot_duration and len(tasks):
            for task in tasks:
                priority.append(eval_priority(start_time, task))
            todo = tasks[priority.index(max(priority))]
            tasks.remove(todo)
            if (todo.duration <= timeslot_duration):
                schedule_dict[todo] = [start_time, start_time + todo.duration]
                timeslot_duration -= todo.duration
                start_time += todo.duration
            else:
                schedule_dict[todo] = [start_time, start_time + timeslot_duration]
                timeslot_duration = 0
                todo.duration -= timeslot_duration
                tasks.append(todo)
    return schedule_dict

# TODO: add_occupied_time
# TODO: convert_available_time: convert occupied time to available_time

test_ddl = "2020, 11, 07, 10, 00"
test_tasks = [Task("test1", convert(test_ddl), 0.5, 30)]
current_time = datetime.now()
test_available_time = [[current_time, convert(test_ddl)]]
print(schedule(test_tasks, test_available_time))
