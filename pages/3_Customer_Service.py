import streamlit as st
from utils.mock_data import get_customer_inquiries

st.set_page_config(page_title="Customer Service | AI Retail Copilot", page_icon="💬", layout="wide")

st.title("💬 Customer Service Support")
st.markdown("AI-assisted responses, returns, and complaint handling.")

inquiries_df = get_customer_inquiries()

# Summary Metrics
open_tickets = len(inquiries_df[inquiries_df['status'] == 'Open'])
high_urgency = len(inquiries_df[inquiries_df['urgency'] == 'High'])

col1, col2 = st.columns(2)
col1.metric("Open Inquiries", open_tickets)
col2.metric("High Urgency", high_urgency)

st.markdown("---")

st.subheader("Active Customer Inquiries")

# Display Tickets
for index, row in inquiries_df.iterrows():
    urgency_color = "red" if row['urgency'] == "High" else "orange" if row['urgency'] == "Medium" else "green"
    
    with st.expander(f"[{row['id']}] {row['customer']} - Category: {row['category']} (Urgency: {row['urgency']})"):
        st.write(f"**Issue:** {row['issue']}")
        st.write(f"**Status:** {row['status']}")
        
        # AI Suggested Response
        st.markdown(f"##### 🤖 Copilot Suggested Response:")
        if row['category'] == 'Shipping':
            ai_draft = f"Hello {row['customer']}, I securely checked your tracking information. Your order is unexpectedly delayed by the carrier but is scheduled to arrive tomorrow. I have expedited shipping on your next order as an apology."
        elif row['category'] == 'Returns':
            ai_draft = f"Hello {row['customer']}, I am sorry the shoes didn't fit! I have automatically generated a return label and sent it to your email. You will be refunded as soon as the package is scanned by the carrier."
        else:
            ai_draft = f"Hello {row['customer']}, let me help you with your {row['category'].lower()} issue. Could you provide the serial number of the device?"
            
        st.info(ai_draft)
        
        c1, c2 = st.columns([1, 4])
        c1.button("Send AI Response", key=f"send_{index}")
        c2.button("Edit Manually", key=f"edit_{index}")

st.markdown("---")
st.subheader("Returns & Exchanges Flow")
st.info("💡 **Copilot Insight**: 80% of returns this week were due to 'Sizing Issues' in the Footwear category. Consider updating the sizing chart on the product page.")
