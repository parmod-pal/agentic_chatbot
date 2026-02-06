import streamlit as st
from src.langgraphpagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphpagenticai.graph.graph_builder import GraphBuilder
from src.langgraphpagenticai.ui.streamlitui.display_result import DisplayResultStreamlit
from src.langgraphpagenticai.LLMS.groqllm import GroqLLM

def load_langgraph_agentic_ai_app():
    """
    Loads and runs the Langgraph AgenticAI Application with Streamlit UI.
    This function initializes the UI,handle user input,configures the LLM model
    set up the graph based on the selected use case, and display the output while implementing exception handling for robustness
    """

    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error.Unable to load User Input")
        return
    
    user_message = st.chat_input("Enter your message")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_controls_inputs=user_input)
            model = obj_llm_config.get_llm_model()
            
            if not model:
                st.error("LLM model not intialized")
                return 
            
            use_case=user_input.get("selected_use_case")
            if not use_case:
                st.error("no use case selected")
                return

            
            graph_builder = GraphBuilder(model)

            try:
                graph = graph_builder.setup_graph(use_case)
                DisplayResultStreamlit(use_case,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"graph setup fail-{e}")
                return

            

            
        except Exception as e: 
             st.error(f"graph setup fail-{e}")
             return
