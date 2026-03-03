import streamlit as st
from utils.mock_data import get_ai_response

st.set_page_config(page_title="Copilot Chat | AI Retail Copilot", page_icon="🤖", layout="wide")

st.title("🤖 Natural Language AI Interface")
st.markdown("Chat with your business data using Generative AI insights.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your AI Retail Copilot. I can analyze inventory, check sales data, help with customer inquiries, and provide predictive business insights. How can I help you today?"}
    ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask about sales, inventory, or customers..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Analyzing business data..."):
            response = get_ai_response(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Quick Suggestion Buttons
st.markdown("---")
st.markdown("**Suggested Queries:**")

def process_query(query):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.spinner("Analyzing business data..."):
        response = get_ai_response(query)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Are there any inventory stockout risks?"):
        process_query("Are there any inventory stockout risks?")
with col2:
    if st.button("How are our recent sales?"):
        process_query("How are our recent sales?")
with col3:
    if st.button("Any pending customer returns?"):
        process_query("Any pending customer returns?")
