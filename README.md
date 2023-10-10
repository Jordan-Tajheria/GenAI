# GenAI ChatBot

This repo holds code for a chatbot built using OpenAI API, which is used for ChatGPT. It can produce rudimentary answers for questions based on the provideded dataset. This application was done using the following tutorial: https://www.youtube.com/watch?v=tjeti5vXWOU as well as various other documentation

## To run on your local device the following should be installed. NOTE: Make sure that wherever the interpreter is pointing to, that the packages are installed in that location i.e. if running from the virtual environment that these are installed in the environment or if running from root that packages are installed globally.

### Python

```
brew install python
```

### Pip

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

### Streamlit - https://docs.streamlit.io/library/get-started/installation

```
pip install streamlit
```

### Langchain

```
pip install langchain
```

### Dotenv

```
pip install python-dotenv
```

### OpenAI

```
pip install --upgrade openai
```

### Tabulate (May be required)

```
pip install tabulate
```

## Important

In order to avoid exposing the API Token it is not added in this repository. Furthmore once the API token becomes exposed it is disabled by OpenAI, causing the applicatioon not to work until a new one is generated and passed through. You will need to get an OpenAI API Key and add it to the:

```
.env file
```

## Running the app

To run the application you will need to execute the main.py file. This is done using the Streamlit CLI, so ensure you have it installed PRIOR to attempting to run the app.

Run the following command in your terminal:

```
streamlit run main.py
```

Download the dataset onto your local and upload it when prompted by the UI, so it can use it as part of its LLM.
https://github.com/nailson/ifood-data-business-analyst-test/blob/master/ml_project1_data.csv
