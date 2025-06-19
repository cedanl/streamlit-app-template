import streamlit as st
from backend.example_task import add_task, get_tasks, update_task_status, delete_task

# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------
title = "example Task"
icon = ":material/folder:"

# ---------------------------------------
# PAGE ELEMENTS
# ---------------------------------------
st.title("✅ Task Manager")
st.balloons()

# Add new task
st.subheader("Add New Task")
with st.form("add_task"):
    title = st.text_input("Task Title")
    description = st.text_area("Description")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    
    if st.form_submit_button("Add Task"):
        if title:
            add_task(title, description, priority)
            st.success("Task added successfully!")
        else:
            st.error("Please enter a task title")

# Display tasks
st.subheader("Tasks")
tasks = get_tasks()

if not tasks:
    st.info("No tasks yet. Add one above!")

for task in tasks:
    with st.container():
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        
        with col1:
            if task['completed']:
                st.write(f"~~{task['title']}~~ ✅")
            else:
                st.write(f"**{task['title']}**")
            if task['description']:
                st.write(f"*{task['description']}*")
        
        with col2:
            color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
            st.write(color.get(task['priority'], '') + task['priority'])
        
        with col3:
            if st.button("Toggle", key=f"toggle_{task['id']}"):
                update_task_status(task['id'], not task['completed'])
                st.rerun()
        
        with col4:
            if st.button("Delete", key=f"del_{task['id']}"):
                delete_task(task['id'])
                st.rerun()
        
        st.divider()