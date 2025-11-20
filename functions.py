def get_tasks( filepath: str = 'task_data.txt' ) -> list:
    ''' Read a text file and return the list of tasks '''
    with open( filepath, 'r' ) as task_file:
        task_list = task_file.readlines()
    return task_list

def write_tasks( tasks_arg: list , filepath: str = 'task_data.txt' ) -> None:
    ''' Writes a list of tasks out to a text file '''
    with open( filepath, 'w' ) as task_file:
        task_file.writelines( tasks_arg )