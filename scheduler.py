from datetime import datetime, timedelta
from math import exp

UUID2Name = {}

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
        self.UUID = hash(name + str(ddl))
        UUID2Name[self.UUID] = name
        self.name = name
        self.ddl = ddl
        self.weight = weight
        self.duration = timedelta(minutes=duration)

def convert(ddl):
    ddl = ddl.split(',')
    return datetime(int(ddl[0]), int(ddl[1]), int(ddl[2]), int(ddl[3]), int(ddl[4]))

def eval_priority(start_time, task):
    # negative???
    ddl_pressure = 1/((task.ddl - start_time - task.duration).total_seconds()/60)
    return exp(task.weight) * ddl_pressure

def schedule(tasks, available_time):
    """([Tasks], [[datetime,datetime]]) -> {Task:[[datetime,datetime]]}
    Parameters:
    tasks:         : list of tasks
    available_time : two-dimensional array of [[begin,end]]
    Return:
    schedule_dict  : dict of task to two-dimensional array of [[begin,end]]
    """
    schedule_dict = {}
    for timeslot in available_time:
        for task in tasks:
            if task.ddl < available_time[0][0]:
                print("{} is overdue\n".format(task.name))
                tasks.remove(task)
            start_time = timeslot[0]
        timeslot_duration = timeslot[1] - timeslot[0]
        while timeslot_duration and len(tasks):
            priority = []
            for task in tasks:
                priority.append(eval_priority(start_time, task))

            print(priority)

            todo = tasks[priority.index(max(priority))]
            tasks.remove(todo)
            priority.remove(max(priority))

            if todo.duration <= timeslot_duration:
                duration = todo.duration
                timeslot_duration -= todo.duration
                new_start_time = start_time + todo.duration
            else:
                duration = timeslot_duration
                todo.duration -= timeslot_duration
                timeslot_duration = 0
                tasks.append(todo)

            time_span = schedule_dict.get(todo.UUID)
            if time_span is None:
                time_span = []
            time_span.append([start_time, start_time + duration])
            schedule_dict[todo.UUID] = time_span
            start_time = new_start_time

    return schedule_dict

def pretty_print(test_tasks, test_available_time):
    schedule_dict = schedule(test_tasks, test_available_time)
    for task_UUID, schedules in schedule_dict.items():
        print(UUID2Name[task_UUID], "is schedule between")
        for start_end in schedules:
            print("start:", str(start_end[0])[0:16])
            print("end  :", str(start_end[1])[0:16])

def last_ddl(test_tasks):
    ddl = [test_task.ddl for test_task in test_tasks]
    return max(ddl)

def add_occupied_time(occupied_time, timeslots, frequency=None):
    if frequency is None:
            if occupied_time[0] <= timeslots[0][0] <= occupied_time[1]:
                removed = timeslots[0]
                timeslots.remove(timeslots[0])
                timeslots.insert(0, [occupied_time[1], removed[1]])
            for i in range(len(timeslots)):
                if timeslots[i][0] <= occupied_time[0] and timeslots[i][1] >= occupied_time[1]:
                    removed = timeslots[i]
                    timeslots.remove(timeslots[i])
                    if removed[1] != occupied_time[1]:
                        timeslots.insert(i, [occupied_time[1],removed[1]])
                    if removed[0] != occupied_time[0]:
                        timeslots.insert(i, [removed[0],occupied_time[0]])
            if occupied_time[0] <= timeslots[-1][1] <= occupied_time[1]:
                timeslots[-1][1] = occupied_time[0]
    else:
        while (occupied_time[0] < timeslots[-1][1]):
            if occupied_time[0] <= timeslots[0][0] <= occupied_time[1]:
                removed = timeslots[0]
                timeslots.remove(timeslots[0])
                timeslots.insert(0, [occupied_time[1], removed[1]])
            for i in range(len(timeslots)):
                if timeslots[i][0] <= occupied_time[0] and timeslots[i][1] >= occupied_time[1]:
                    removed = timeslots[i]
                    timeslots.remove(timeslots[i])
                    if removed[1] != occupied_time[1]:
                        timeslots.insert(i, [occupied_time[1],removed[1]])
                    if removed[0] != occupied_time[0]:
                        timeslots.insert(i, [removed[0],occupied_time[0]])
            if occupied_time[0] <= timeslots[-1][1] <= occupied_time[1]:
                timeslots[-1][1] = occupied_time[0]
            occupied_time[0] += frequency
            occupied_time[1] += frequency
    for timeslot1,timeslot2 in timeslots:
        print(timeslot1)
        print(timeslot2)
        print('\n')
    return timeslots