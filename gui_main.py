import functions as func
import FreeSimpleGUI as fsg

loop = True

func.init_data()

label = fsg.Text( 'Type in a task' )
input_box = fsg.InputText( tooltip = 'Enter a task', key = 'task' )
add_button = fsg.Button( 'Add' )
edit_button = fsg.Button( 'Edit' )

window = fsg.Window( 'Task List App', 
                    layout = [[label, input_box, add_button]],
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
            
        case fsg.WINDOW_CLOSED:
            break
            


window.close()