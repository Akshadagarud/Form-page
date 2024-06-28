import streamlit as st

# Set up the form
st.title('User Information Form')

with st.form(key='user_form'):
    name = st.text_input('Name')
    phone_number = st.text_input('Phone Number')
    email_id = st.text_input('Email ID')
    field = st.checkbox('Field')
    location = st.text_input('Location')
    domain = st.selectbox('Domain', ['Data science', 'ML', 'Other'])
    
    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Display the submitted form data
if submit_button:
    st.write('Form submitted successfully!')
    st.write('Name:', name)
    st.write('Phone Number:', phone_number)
    st.write('Email ID:', email_id)
    st.write('Field (Book):', field)
    st.write('Location:', location)
    st.write('Domain:', domain)