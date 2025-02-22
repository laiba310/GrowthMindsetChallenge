import streamlit as st

def show_todolist():
    st.title("Simple Todo List")

    if 'tasks' not in st.session_state:
        st.session_state['tasks'] = []

  
    def add_task():
        task = st.text_input("Enter a task", "")
        if st.button("Add Task") and task != "":
            st.session_state.tasks.append(task)
            st.rerun()

    
    def remove_task(task):
        st.session_state.tasks.remove(task)
        st.rerun()

    add_task()

    if st.session_state.tasks:
        # Heading for the tasks
        st.write("### Your Todo List:")

       
        for task in st.session_state.tasks:
           
            col1, col2 = st.columns([9, 1])

            # Task text on the left side
            with col1:
                st.write(f"- {task}")

            # Remove button on the right side
            with col2:
                if st.button("Remove", key=task):
                    remove_task(task)

               
                st.markdown("""
                    <style>
                        .stButton button {
                           font-size: 18px;
            font-weight: bold;
            color: white;
            background: #008CBA;
            border-radius: 10px;
            padding: 8px 20px;
            margin: 5px;
            border: none;
        word-break: normal !important;
        white-space: nowrap !important;
                        }
                        .stButton button:hover {
                            background-color: #2b6cb0;
                        }
                    </style>
                """, unsafe_allow_html=True)
    else:
       
        st.write("No tasks added yet!")

