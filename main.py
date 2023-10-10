import streamlit as st

from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv


def main():

    load_dotenv()

    #Let streamlit know that this is a streamlit application
    st.set_page_config(page_title="Generative AI Chatbot")
    st.header("Generative AI Chatbot")

    #Store in an object
    user_csv = st.file_uploader("Upload your CSV file", type="csv")

    #Check if the user has provided a dataset, in this case a csv file
    if user_csv is not None:
        user_question = st.text_input("Ask any question about your CSV")

        #Initialise the LLM, 0=non-creative, 1=creative (I.e returning a different answer each time)
        llm = OpenAI(temperature=0)
        #Verbose set to true will display the thinking/thought process the model is undertaking whilst
        # generating the answer.
        agent = create_csv_agent(llm, user_csv, verbose=True)

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            #st.write(f"Your question was: {user_question}")
            st.write(response)

#Test whether we are importing the application
if __name__ == "__main__":
    main()