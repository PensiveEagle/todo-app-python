task_prompt = "Enter a task: "

loop = True
task_list = []

while loop:
    task = input(task_prompt)
    task_list.append(task)
    print( task_list )