import streamlit as st
import functions as func

tasks = func.get_tasks( filepath = "task_data.txt" )

st.title( "Simple To Do App" )
st.subheader( "by PensiveEagle" )
st.write( "This is an example app that allows a user to track tasks" )

for task in tasks:
    st.checkbox( task )
    
st.text_input( label = "", placeholder = "Enter a new task..." )