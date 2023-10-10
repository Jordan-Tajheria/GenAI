import streamlit as st

def main():
    #Let streamlit know that this is a streamlit application
    st.set_page_config(page_title="Generative AI Chatbot")
    st.header("Generative AI Chatbot")

    #Store in an object
    user_csv = st.file_uploader("Upload your CSV file", type="csv")


#Test whether we are importing the application
if __name__ == "__main__":
    main()