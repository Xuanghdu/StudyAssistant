from scheduler import add_occupied_time, schedule, Task

from datetime import datetime

DATETIME_MAX = datetime(2049, 12, 31, 23, 59)

UPCOMING_COUNT_MAX = 20
'''Maximum number of tasks shown in the "Upcoming tasks" list.'''

fixedTimeTasks = []
'''2-dimensional array of fixed time task. In each row, there are `taskName`,
`startTime`, and `endTime` correspondingly.'''

floatingTimeTasks = []
'''1-dimensional array of Task objects.'''

floatingSchedule = {}
'''Dictionary from Task UUIDs to two dimensional arrays. Each row of the array
represents an assigned time slot.'''

upcomingTasks = {}
'''2-dimensional array of upcoming tasks. In each row, there are task name,
start time, and end time correspondingly.'''


class FixedTimeOverlapException(Exception):
    '''Throwed only when `addFixedTimeTask` function encounters a
    time-overlapping issue.

    It holds the name of the overlapping task.'''

    pass


class FloatingTimeOverlapException(Exception):
    '''Throwed only when `addFloatingTimeTask` function fails to schedule a new
    task.

    It (maybe) hold the UUID/name of the overlapping task.'''


def isTimeSlotOverlap(start1, end1, start2, end2):
    '''Accept four datetime objects, and return `true` if the two time slots
    overlap.'''

    return end1 > start2 and end2 > start1


def addFixedTimeTask(taskName, startTime, endTime):
    '''Add a fixed-time task.

    `taskName` is a non-empty string. `startTime` and `endTime` are two datetime
    objects.

    It throws a FixedTimeOverlapException if the given timeslot is illegal.'''

    for name2, start2, end2 in fixedTimeTasks:
        if isTimeSlotOverlap(startTime, endTime, start2, end2):
            raise FixedTimeOverlapException(name2)

    fixedTimeTasks.append([taskName, startTime, endTime])


def getAvailableTimeSlots(now=None):
    '''Given the "now" time, return a 2-dimensional array of vailable time
    slots.'''

    if now is None:
        now = datetime.now()
    available = [[now, DATETIME_MAX]]
    for _, startTime, endTime in fixedTimeTasks:
        available = add_occupied_time([startTime, endTime], available)
    return available


def addFloatingTimeTask(task):
    '''Add a floating-time task and update the schedule. The input value is a
    Task object.

    It throws a FloatingTimeOverlapException if the scheduling algorithm
    fails.'''

    floatingTimeTasks.append(task)
    availableTime = getAvailableTimeSlots()

    newSchedule = schedule(floatingTimeTasks, availableTime)
    # TODO: pass the UUID/name of overlapping task into the exception
    if newSchedule is None:
        raise FloatingTimeOverlapException()

    floatingSchedule = newSchedule


def updateUpcomingTasks(now=None):
    '''Given the "now" time, update `upcomingTasks`.'''

    if now is None:
        now = datetime.now()

    tupleList = []
    for task in fixedTimeTasks:
        tupleList.append((task[1], task[0], task[2]))
    for task in floatingTimeTasks:
        name = task.name
        timeSlots = floatingSchedule[task.UUID]
        for startTime, endTime in timeSlots:
            tupleList.append((startTime, name, endTime))
    tupleList.sort()

    while len(tupleList) and tupleList[0][0] <= now:
        del tupleList[0]
    if len(tupleList) > UPCOMING_COUNT_MAX:
        tupleList = tupleList[0:UPCOMING_COUNT_MAX]
    # TODO: Handle the case when multiple tasks have the same start time.

    upcomingTasks = []
    for startTime, name, endTime in tupleList:
        upcomingTasks.append([name, startTime, endTime])
