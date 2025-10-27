task_prompt = "Enter a task: "
action_prompt = "Type add, show, edit, or exit: "
grab_prompt = "Which item would you like to edit?: "
edit_prompt = "Enter new task: "

loop = True
task_list = []

while loop:
    action = input( action_prompt )
    action = action.strip()
    
    match action:
        case 'add':
            new_task = input( task_prompt )
            task_list.append( new_task )
            print( f'{new_task} added to list!' )
        case 'show':
            for item in task_list:
                print( f'+ {item}' )
        case 'edit':
            for item in task_list:
                print( f'+ {item}' )
            grab_task = int( input( grab_prompt ) ) - 1
            edit_task = input( edit_prompt )
            task_list[grab_task] = edit_task
        case 'exit':
            break