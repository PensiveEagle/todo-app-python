import functions as func
import FreeSimpleGUI as fsg

label = fsg.Text( 'Type in a task' )
input_box = fsg.InputText( tooltip = 'Enter a task', default_text = 'New task' )
add_button = fsg.Button( 'Add' )

window = fsg.Window( 'Task List App', layout = [[label], [input_box, add_button]] )
window.read()
window.close()