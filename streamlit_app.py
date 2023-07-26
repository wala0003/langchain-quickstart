import streamlit as st
import langchain
import langchain.tools
from langchain.tools import BaseTool
from scrapingbee import ScrapingBeeClient
from trafilatura import extract
from langchain.llms import OpenAI

class ScrapingBeeTool(BaseTool):

    def __init__(self, api_key):
        self.api_key = api_key
        self.client = ScrapingBeeClient(self.api_key)
        
    def run(self, prompt):
        response = self.client.get(url=prompt, proxy=True)
        extracted = extract(response.content)
        llm = OpenAI(temperature=0.7) 
        return llm.generate(extracted)

# Streamlit app
st.set_page_config(page_title="Web Summary")
st.title("Web Page Summarizer")

# Sidebar for API keys
st.sidebar.title('API Keys')
scrapingbee_key = st.sidebar.text_input('ScrapingBee API Key')
openai_key = st.sidebar.text_input('OpenAI API Key') 

url = st.text_input('Enter a URL to summarize:')

if st.button('Get Summary'):
    tool = ScrapingBeeTool(api_key=scrapingbee_key)
    llm = OpenAI(openai_key, temperature=0.7)
    summary = tool.run(url)
    
    st.write(summary)
