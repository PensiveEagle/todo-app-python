import functions as func
import FreeSimpleGUI as fsg
import time

func.init_data()

fsg.theme( 'System Default' )

clock_label = fsg.Text( time.strftime( '%Y-%m-%d -- %H:%M' ), key = 'clock' )
task_label = fsg.Text( 'Type in a task' )
input_box = fsg.InputText( tooltip = 'Enter a task', key = 'task' )
add_button = fsg.Button( 'Add' )
edit_button = fsg.Button( 'Edit' )
complete_button = fsg.Button( 'Complete' )
exit_button = fsg.Button( 'Exit' )
task_list_box = fsg.Listbox( values = func.get_tasks(), 
                            key = "tasks", 
                            enable_events = True,
                            size = [45, 10]
                            ) # type: ignore

win_layout = [
    [clock_label],
    [task_label], 
    [input_box, add_button],
    [task_list_box, edit_button, complete_button],#
    [exit_button]
]

window = fsg.Window( 'Task List App', 
                    layout = win_layout,
                    font = ( 'Helvetica', 12 ) )


while True:
    event, values = window.read( timeout = 60000 ) #type: ignore
    
    match event:
        
        case 'Add':
            task_list = func.get_tasks()
            new_task = values['task']
            task_list.append( new_task + '\n' )
            func.write_tasks( task_list )
            window['task'].update( value = '' ) #type: ignore
            window['tasks'].update( values = func.get_tasks() ) #type: ignore
            
        case 'Edit':
            try:
                task_list = func.get_tasks()
                edit_task = values['tasks']
                new_task = values['task']
                edit_index = task_list.index( edit_task[0] )
                task_list[edit_index] = new_task + '\n'
                func.write_tasks( task_list )
                window['task'].update( value = '' ) #type: ignore
                window['tasks'].update( values = task_list ) #type: ignore
            except IndexError:
                print( 'WARNING: No item was selected when edit button was pressed' )
                fsg.popup( 'Please select a task before editting!', title = 'Error', font = ('Helvetica', 12) )
                continue
            
        case 'Complete':
            try:
                task_list = func.get_tasks()
                complete_task = values['tasks']
                complete_index = task_list.index( complete_task[0] )
                task_list.pop( complete_index )
                func.write_tasks( task_list )
                window['task'].update( value = '' ) #type: ignore
                window['tasks'].update( values = task_list ) #type: ignore
            except IndexError:
                print( 'WARNING: No item was selected when complete button was pressed' )
                fsg.popup( 'Please select a task before completing!', title = 'Error', font = ('Helvetica', 12) )
                continue
            
        case 'tasks':
            window['task'].update( value = values['tasks'][0].replace( '\n', '' ) ) #type: ignore
            
        case 'Exit':
            break
            
        case fsg.WIN_CLOSED:
            break
        
    window['clock'].update( value = time.strftime( '%Y-%m-%d -- %H:%M' ) ) #type: ignore
            
window.close()

'''
______
   |  |
   |__|
   |  |
\_/|  |

'''
