task_prompt = "Enter a task: "
action_prompt = "Type add, show, edit, complete, or exit: "
grab_prompt = "Which item would you like to edit/complete?: "
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
            print( f'\n{new_task} added to list!\n' )
            
        case 'show':
            print()
            for index, item in enumerate(task_list):
                print( f'{index + 1}:- {item}' )
            print()
            
        case 'edit':
            print()
            for index, item in enumerate(task_list):
                print( f'{index + 1}:- {item}' )
            print()
            
            grab_task = int( input( grab_prompt ) ) - 1
            print( f'\nCurrent task: {task_list[grab_task]}\n' )
            
            edit_task = input( edit_prompt )
            print()
            task_list[grab_task] = edit_task
            
        case 'complete':
            print()
            grab_task = int( input( grab_prompt ) ) - 1
            task_list.pop(grab_task)
            print()
            
        case 'exit':
            break
        
print( f'\nClosing To Do App!!\n' )