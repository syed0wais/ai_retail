import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(
    page_title="AI Retail Copilot",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("AI Retail Copilot")
st.markdown("### Intelligent Assistant for Retail & SMBs")

st.markdown("""
Welcome to the **AI Retail Copilot**! This platform leverages predictive analytics and Generative AI concepts to help you run your business efficiently.

**Features Available:**
*   📈 **Dashboard**: High-level overview of business KPIs.
*   📦 **Inventory Management**: Real-time stock monitoring and reorder alerts.
*   💬 **Customer Service**: AI-assisted responses and complaint handling.
*   📊 **Sales Analytics**: Deep dive into revenue and product performance.
*   🚚 **Order Processing**: Management of fulfillments and validations.
*   🤖 **AI Copilot Chat**: Natural language interface for business insights.

Please use the sidebar to navigate through the modules.
""")

# Decorative image or aesthetic elements
st.info("💡 **Copilot Tip**: Head over to the **AI Copilot Chat** to ask natural language questions about your business performance!")
