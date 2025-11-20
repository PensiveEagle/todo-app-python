prompts = {'task': 'Enter a task: ', 'action': 'Type add, show, edit, complete, or exit: ', 'grab': 'Which item would you like to edit/complete?: ', 'edit': 'Enter new task: '}

import functions
import time
    
loop = True

functions.init_data()

now = time.strftime("%Y-%m-%d %H:%M")

print( f"Welcome to the task manager! - {now}" )


while loop:
    action = input( prompts['action'] )
    
    if 'add' in action:
        new_task = action[4:]
            
        task_list = functions.get_tasks()
        
        task_list.append( new_task + '\n' )
        
        functions.write_tasks( task_list )
    
    elif 'show' in action:
        task_list = functions.get_tasks()
        
        for index, item in enumerate(task_list):
            print( f'{index + 1}:- {item}' )
    
    elif 'edit' in action:
        try:
            task_list = functions.get_tasks()
            
            grab_task = int( action[5:] ) - 1
            old_task = task_list[grab_task]
            
            edit_task = input( prompts['edit'] )
            task_list[grab_task] = edit_task + '\n'
            
            functions.write_tasks( task_list )
        
        except ValueError:
            print( "Your command was invalid!" )
            continue
    
    elif 'complete' in action:
        try:
            task_list = functions.get_tasks()
            
            grab_task = int( action[9:] ) - 1
            complete_task = task_list[grab_task]
            task_list.pop( grab_task )
            
            functions.write_tasks( task_list )
            
        except ValueError:
            print( "Your command was invalid!" )
            continue

    elif 'exit':
        break
    
print( f'\nClosing To Do App!!\n' )