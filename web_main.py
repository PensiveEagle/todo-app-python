import streamlit as st
import functions as func

func.init_data()

tasks = func.get_tasks()

def add_task():
    task = st.session_state["new_task"] + "\n"
    tasks.append( task )
    func.write_tasks( tasks )


st.title( "Simple To Do App" )
st.subheader( "by PensiveEagle" )
st.write( "This is an example app that allows a user to track tasks" )

for task in tasks:
    st.checkbox( task )
    
st.text_input( label = "Enter a new task", 
              placeholder = "Enter a new task...",
              label_visibility = "hidden",
              on_change = add_task,
              key = "new_task" )