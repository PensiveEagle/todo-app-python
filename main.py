prompts = {'task': 'Enter a task: ', 'action': 'Type add, show, edit, complete, or exit: ', 'grab': 'Which item would you like to edit/complete?: ', 'edit': 'Enter new task: '}

loop = True

with open( 'task_data.txt', 'a' ) as task_file:
    pass

while loop:
    action = input( prompts['action'] )
    
    if 'add' in action:
        new_task = action[4:]
            
        with open( 'task_data.txt', 'r' ) as task_file:
            task_list = task_file.readlines()
        
        task_list.append( new_task )
        
        with open( 'task_data.txt', 'w' ) as task_file:
            task_file.writelines( task_list )
                
            print( f'\n{new_task} added to list!\n' )
    
    elif 'show' in action:
        with open( 'task_data.txt', 'r' ) as task_file:
            task_list = task_file.readlines()
        
        print()
        for index, item in enumerate(task_list):
            print( f'{index + 1}:- {item}' )
        print()
    
    elif 'edit' in action:
        with open( 'task_data.txt', 'r' ) as task_file:
            task_list = task_file.readlines()
        
        grab_task = int( action[5:] ) - 1
        old_task = task_list[grab_task]
        print( f'\nCurrent task: {old_task}\n' )
        
        edit_task = input( prompts['edit'] )
        print()
        task_list[grab_task] = edit_task
        
        with open( 'task_data.txt', 'w' ) as task_file:
            task_file.writelines( task_list )
            
        print( f'\n{old_task} replaced with {edit_task}\n' )
    
    elif 'complete' in action:
        with open( 'task_data.txt', 'r' ) as task_file:
            task_list = task_file.readlines()
        
        grab_task = int( action[5:] ) - 1
        complete_task = task_list[grab_task]
        task_list.pop( grab_task )
        
        with open( 'task_data.txt', 'w' ) as task_file:
            task_file.writelines( task_list )
        
        print( f'\n{complete_task} marked as complete!\n' )

    elif 'exit':
        break
    
print( f'\nClosing To Do App!!\n' )