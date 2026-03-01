import streamlit as st

st.set_page_config(page_title="AWS Architecture | AI Retail Copilot", page_icon="☁️", layout="wide")

st.title("☁️ Architecture & AWS Integration")
st.markdown("---")

st.markdown("""
### Technical Evaluation Criteria: Using Generative AI on AWS

Welcome to the **AI Retail Copilot**! We are proud to participate in the **AI for Bharat Hackathon**. This application has been architected to align with the core evaluation criteria for AWS Generative AI services.

#### 1. Why is AI Required?
In the modern retail ecosystem, store owners are overwhelmed by scattered data streams—from inventory counts to daily sales and unstructured customer feedback. AI is essential here because it acts as an **Intelligent Synthesizer**. It translates this raw, multi-channel data into plain-language business intelligence, enabling owners to make rapid, data-driven decisions without needing a data science background.

#### 2. How are AWS Services Used?
This application leverages **AWS-native patterns** for scalability, security, and advanced AI capabilities:
*   **Amazon Bedrock**: We use Amazon Bedrock to access foundation models (specifically `anthropic.claude-v2`). Bedrock serves as the brain of our **AI Copilot Chat**, providing secure, serverless generative AI inferences over our real-time retail data.
*   **Infrastructure (Conceptual/Future State)**: The app is designed to be deployed on **Amazon EC2** or **AWS Amplify** for frontend hosting, backing its robust mock data with a scalable **Amazon DynamoDB** database for actual production inventory state.

#### 3. What Value Does the AI Layer Add?
The Amazon Bedrock AI layer transforms the application from a simple dashboard into a proactive **Copilot**:
*   **Automates Customer Service**: Rapidly processes and suggests resolutions for customer complaints.
*   **Predicts Stockouts**: Analyzes current stock versus demand to generate natural-language reorder alerts.
*   **Accessible Insights**: Allows the user to simply ask "How are our recent sales?" and get a highly contextualized, instant response.

---
""")

# Celebrate achievement badge
st.info("""
🎉 **Achievement Unlocked!**

"I am excited to be architecting the future of Bharat as a Prototype Developer in the AI for Bharat Hackathon! 🚀"
""")
