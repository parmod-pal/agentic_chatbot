import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self, use_case, graph, user_message):
        self.usecase = use_case
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase.lower().strip()
        graph = self.graph
        user_message = self.user_message
        if usecase == "basic chatbot":
            with st.chat_message("user"):
                st.write(user_message)
            
            try:
                for event in graph.stream({'messages': [HumanMessage(content=user_message)]}):
                    for key, value in event.items():
                        if key == "chatbot" and "messages" in value:
                            with st.chat_message("assistant"):
                                if isinstance(value["messages"], list):
                                    st.write(value["messages"][-1].content)
                                else:
                                    st.write(value["messages"].content)
            except Exception as e:
                st.error(f"Error streaming graph: {e}")