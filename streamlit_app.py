import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.tools import DuckDuckGoSearchRun
from langchain.tools import YouTubeSearchTool


openai_api_key = st.sidebar.text_input('OpenAI API Key')

# Initialize your LLM Model
#Create an instance of OpenAI LLM
llm = ChatOpenAI(model_name='gpt-3.5-turbo',openai_api_key=openai_api_key ,temperature=0.1)

# build a tool to search the internet
search = DuckDuckGoSearchRun()
yt = YouTubeSearchTool()
search_tool = Tool(name="search_tool", description = "search the internet",func = search.run)
yt_tool= Tool( name='Youtube', description="search youtube videos",func= yt.run)
tools = [search_tool,yt_tool]

#build our agent
agent = initialize_agent(tools, llm, agent='zero-shot-react-description',verbose=True)

st.title('Langchain Search GPT tester')
# Create a text input box for the user
#Create a  Propmt 
prompt = st.text_input('Input your prompt here')


# If user hits enter
if prompt:
  response =agent.run(prompt)
  st.write(response)
