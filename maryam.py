import streamlit as st
import pickle

def load_tasks():
    try:
        with open("tasks.pkl", "rb") as f:
            tasks = pickle.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.pkl", "wb") as f:
        pickle.dump(tasks, f)

def main():
    st.title("Efficient To-Do List App")
    st.write("Welcome to your personal to-do list!")

    tasks = load_tasks()

    task = st.text_input("Add a new task:")
    if st.button("Add"):
        tasks.append(task)
        save_tasks(tasks)

    st.write("### Current Tasks")
    if not tasks:
        st.write("No tasks added yet.")
    else:
        for i, task in enumerate(tasks):
            st.write(f"{i + 1}. {task}")

    if st.button("Clear All"):
        tasks = []
        save_tasks(tasks)

if __name__ == '__main__':
    main()
