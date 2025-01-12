import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from pdf_loader import pdf_database
from prompt import PROMPT
from langchain_core.messages import *
load_dotenv()

# print(ChatOpenAI().invoke("hello").content)

@tool
def pdf_db(question):
    """
    get the data when ever you are asked about chemistry related questions
    get the data by passing well formatted question
    """
    return pdf_database(question)

tools = [pdf_db]
model = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)

messages = [SystemMessage(PROMPT)]

def chat(question):
    messages.append(HumanMessage(question))
    response = model.invoke(messages)
    messages.append(response)

    if response.tool_calls:
        for tool_call in response.tool_calls:
                if tool_call['name'] == "pdf_db":
                    messages.append(ToolMessage(pdf_db(tool_call['args']['question']),tool_call_id=tool_call["id"]))
        
        response = model.invoke(messages)
        messages.append(response)
    
    return response.content