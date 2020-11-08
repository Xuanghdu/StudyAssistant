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
    # avoid exact 0
    # avoid negative (in the middle of calculation)
    if (task.ddl - start_time - task.duration).total_seconds() <= 0:
        ddl_pressure = 2
    else:
        ddl_pressure = 1 / \
            ((task.ddl - start_time - task.duration).total_seconds()/60)
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

    # shrink duration according to deadlines:
    #   starting from the first deadline
    #   shrink all durations before an unmeetable deadline
    #   shrink by weight factor

    deadlines = sorted(list(set([task.ddl for task in tasks])))
    for ddl in deadlines:
        # total_time_for_slot = sum([task.duration for task in tasks])
        total_duration = timedelta(minutes=0)
        weighted_total_duration = timedelta(minutes=0)

        for task in tasks:
            if task.ddl <= ddl:
                total_duration += task.duration
                weighted_total_duration += 1 / \
                    (1+exp(-task.weight)) * task.duration

        ddl_time_left = timedelta(minutes=0)
        for start, end in available_time:
            if end < ddl:
                ddl_time_left += end-start
            elif start < ddl:
                ddl_time_left += ddl-start
            else:
                break

        if total_duration > ddl_time_left:
            for task in tasks:
                if task.ddl <= ddl:
                    task.duration *= 0.9*1 / \
                        (1+exp(-task.weight)) * \
                        ddl_time_left/weighted_total_duration

    # for task in tasks:
    #     print(task.duration)

    for timeslot in available_time:
        for task in tasks:
            if task.ddl < available_time[0][0]:
                print("{} is overdue\n".format(task.name))
                tasks.remove(task)

        redo_this_time_slot = 1
        shrink = 0
        fatal_deadline = None
        while redo_this_time_slot:
            redo_this_time_slot = 0

            if shrink:
                for task in tasks:
                    print('performing shrink')
                    if task.ddl <= fatal_deadline:
                        task.duration *= 0.1*task.weight+0.85
                    print(task.UUID, ":", task.duration)
                print('final--', fatal_deadline)

            start_time = timeslot[0]
            timeslot_duration = timeslot[1] - timeslot[0]

            arranged = []
            priority_bonus = {}  # initialize bonus dict
            for task in tasks:
                priority_bonus[task.UUID] = 1

            while timeslot_duration and len(tasks):

                priority = []
                for task in tasks:
                    # multiply by bonus
                    priority.append(eval_priority(
                        start_time, task)*priority_bonus[task.UUID])

                # print(priority)

                todo = tasks[priority.index(max(priority))]

                # redo if cannot fit
                # print(todo.ddl)
                if (todo.ddl - start_time - todo.duration).total_seconds() < 0:
                    if not len(arranged):
                        print("Impossible to fit")

                        redo_this_time_slot = 1
                        shrink = 1
                        fatal_deadline = todo.ddl
                        break

                    previous_todo = arranged.pop()
                    tasks.append(previous_todo)
                    time_span = schedule_dict.get(previous_todo.UUID)
                    start_time, end_time = time_span.pop()
                    timeslot_duration += end_time-start_time
                    schedule_dict[previous_todo.UUID] = time_span
                    # brute force to increase priority while keeping weight unchanged
                    priority_bonus[todo.UUID] *= 2
                    continue

                arranged.append(todo)  # add redo point
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
                    # added this don't know if any bug would happen
                    new_start_time = start_time + todo.duration

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
                    timeslots.insert(i, [occupied_time[1], removed[1]])
                if removed[0] != occupied_time[0]:
                    timeslots.insert(i, [removed[0], occupied_time[0]])
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
                        timeslots.insert(i, [occupied_time[1], removed[1]])
                    if removed[0] != occupied_time[0]:
                        timeslots.insert(i, [removed[0], occupied_time[0]])
            if occupied_time[0] <= timeslots[-1][1] <= occupied_time[1]:
                timeslots[-1][1] = occupied_time[0]
            occupied_time[0] += frequency
            occupied_time[1] += frequency
    for timeslot1, timeslot2 in timeslots:
        print(timeslot1)
        print(timeslot2)
        print('\n')
    return timeslots
