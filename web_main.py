import streamlit as st
import functions as func

st.title( "Simple To Do App" )
st.subheader( "by PensiveEagle" )
st.write( "This is an example app that allows a user to track tasks" )

tasks = func.get_tasks( filepath = "task_data.txt" )

for task in tasks:
    st.checkbox( task )