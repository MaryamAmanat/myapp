import streamlit as st

# Dictionary to store user records
user_records = {}

def signup():
    st.subheader("Create a New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    if st.button("Signup"):
        if new_user in user_records:
            st.warning("Username already exists. Please choose a different username.")
        else:
            user_records[new_user] = new_password
            st.success("Account created successfully. Please login.")

def login():
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in user_records and user_records[username] == password:
            st.success(f"Logged in as {username}")
            show_career_counseling_form()
        else:
            st.error("Invalid username or password.")

def show_career_counseling_form():
    st.subheader("Career Counseling")
    st.write("Please provide the following information:")
    
    hobbies = st.text_input("Hobbies")
    interests = st.text_input("Interests")
    education = st.text_input("Education Level")
    
    if st.button("Submit"):
        # Call a function to process the inputs and suggest careers
        suggested_careers = suggest_careers(hobbies, interests, education)
        
        st.subheader("Suggested Careers")
        for career in suggested_careers:
            st.write(career)

def suggest_careers(hobbies, interests, education):
    # Placeholder function for suggesting careers based on inputs
    # You can replace this with your own career suggestion logic
    suggested_careers = ["Software Engineer", "Graphic Designer", "Data Scientist"]
    return suggested_careers

def main():
    st.title("Career Counseling App")
    st.write("Please login or signup to continue.")

    menu = ["Login", "Signup"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        login()
    elif choice == "Signup":
        signup()

if __name__ == "__main__":
    main()
