import streamlit as st
import requests

st.title("Text Processing App")

# Text input field
user_input = st.text_area("Enter your text here:", height=100)

# Submit button
if st.button("Submit"):
    if user_input:
        # Make request to backend
        try:
            response = requests.post(
                "http://localhost:8000/process",
                json={"text": user_input}
            )
            if response.status_code == 200:
                result = response.json()
                st.write("Response from backend:")
                st.write(result["response"])
            else:
                st.error("Error processing the request")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend server. Make sure it's running.")
    else:
        st.warning("Please enter some text before submitting.") 