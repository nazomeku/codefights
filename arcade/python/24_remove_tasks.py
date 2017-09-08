"""Given the list of task ids in your toDo list, remove each kth task from it
and return the list of remaining tasks."""


def remove_tasks(k, todo):
    del todo[k-1::k]
    return todo
