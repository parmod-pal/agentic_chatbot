import os
import streamlit as st 
from langchain_groq import ChatGroq

class GroqLLM:
    
    def __init__(self,user_controls_inputs):
        self.user_controls_inputs = user_controls_inputs

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_inputs["GROQ_API_KEY"]
            groq_model = self.user_controls_inputs["selected_groq_models"]
            if groq_api_key == '' and os.environ['GROQ_API_KEY'] == '':
                st.error(f"Enter groq Api key")
            
            llm = ChatGroq(api_key=groq_api_key,model=groq_model)

        except Exception as e:
            raise ValueError(f"Error Occured with Exception:{e}")

        return llm