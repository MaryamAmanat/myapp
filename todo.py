import streamlit as st

def get_session_state():
    if not hasattr(st, '_session_state'):
        st._session_state = {'tasks': []}

    return st._session_state

def main():
    st.title("To-Do List App")
    st.write("Welcome to your personal to-do list!")

    session_state = get_session_state()

    task = st.text_input("Add a new task:")
    if st.button("Add"):
        session_state['tasks'].append(task)

    st.write("### Current Tasks")
    for i, task in enumerate(session_state['tasks']):
        st.write(f"{i + 1}. {task}")

    if st.button("Clear All"):
        session_state['tasks'] = []

if __name__ == '__main__':
    main()
