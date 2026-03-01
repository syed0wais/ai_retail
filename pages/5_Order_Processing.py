import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Order Processing | AI Retail Copilot", page_icon="🚚", layout="wide")

st.title("🚚 Order Processing Automation")
st.markdown("Automated order validation, tracking, payment, and shipping guidance.")

# Mock Orders Data
def get_orders():
    orders = [
        {"Order ID": "ORD-1001", "Customer": "John Doe", "Amount": "$125.00", "Status": "Pending Validation", "Fraud Risk": "Low"},
        {"Order ID": "ORD-1002", "Customer": "Jane Smith", "Amount": "$450.00", "Status": "Processing", "Fraud Risk": "Low"},
        {"Order ID": "ORD-1003", "Customer": "Suspicious User", "Amount": "$1,200.00", "Status": "Flagged", "Fraud Risk": "High"},
        {"Order ID": "ORD-1004", "Customer": "Emily Davis", "Amount": "$85.00", "Status": "Shipped", "Fraud Risk": "Low"},
    ]
    return pd.DataFrame(orders)

orders_df = get_orders()

# Top Metrics
st.subheader("Order Status Overview")
c1, c2, c3 = st.columns(3)
c1.metric("Orders Today", len(orders_df))
c2.metric("Processing", len(orders_df[orders_df['Status'].isin(['Pending Validation', 'Processing'])]))
c3.metric("Flagged for Fraud", len(orders_df[orders_df['Status'] == 'Flagged']), delta="High Risk", delta_color="inverse")

st.markdown("---")

# Order Details
st.subheader("Recent Orders")

for index, row in orders_df.iterrows():
    if row['Status'] == 'Flagged':
        st.error(f"⚠️ **{row['Order ID']}** - {row['Customer']} ({row['Amount']}) - Risk: {row['Fraud Risk']}")
        st.markdown("**AI Validation Reason:** Shipping address mismatch and multiple failed payment attempts. Manual review required.")
        st.button(f"Review Order {row['Order ID']}", key=f"btn_{index}")
    elif row['Status'] == 'Pending Validation':
        st.warning(f"⏳ **{row['Order ID']}** - {row['Customer']} ({row['Amount']})")
        st.markdown("**AI Processing:** Validating inventory availability across localized warehouses...")
    else:
        st.success(f"✅ **{row['Order ID']}** - {row['Customer']} ({row['Amount']}) - Risk: {row['Fraud Risk']} - Status: {row['Status']}")

st.markdown("---")
st.subheader("Shipping Guidance Automation")
st.info("💡 **Copilot Route Optimization:** Orders ORD-1002 and ORD-1004 are shipping to the same regional zone. Grouping these under carrier 'FastShip Logistics' will save an estimated 12% on shipping costs.")
