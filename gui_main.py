import functions as func
import FreeSimpleGUI as fsg

loop = True

func.init_data()

label = fsg.Text( 'Type in a task' )
input_box = fsg.InputText( tooltip = 'Enter a task', key = 'task' )
add_button = fsg.Button( 'Add' )
edit_button = fsg.Button( 'Edit' )
task_list_box = fsg.Listbox( values = func.get_tasks(), 
                            key = "tasks", 
                            enable_events = True,
                            size = [45, 10]
                            ) # type: ignore

win_layout = [
    [label], 
    [input_box, add_button],
    [task_list_box, edit_button]
]

window = fsg.Window( 'Task List App', 
                    layout = win_layout,
                    font = ( 'Helvetica', 12 ) )


while loop:
    event, values = window.read() #type: ignore
    print( event )
    print( values )
    
    match event:
        
        case 'Add':
            task_list = func.get_tasks()
            new_task = values['task']
            task_list.append( new_task + '\n' )
            func.write_tasks( task_list )
            window['task'].update( value = '' ) #type: ignore
            window['tasks'].update( values = func.get_tasks() ) #type: ignore
            
        case 'Edit':
            task_list = func.get_tasks()
            edit_task = values['tasks']
            new_task = values['task']
            edit_index = task_list.index( edit_task[0] )
            task_list[edit_index] = new_task + '\n'
            func.write_tasks( task_list )
            window['task'].update( value = '' ) #type: ignore
            window['tasks'].update( values = task_list ) #type: ignore
            
        case 'tasks':
            window['task'].update( value = values['tasks'][0].replace( '\n', '' ) ) #type: ignore
            
        case fsg.WINDOW_CLOSED:
            break
            


window.close()