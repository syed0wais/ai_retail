import streamlit as st
import plotly.express as px
from utils.mock_data import get_sales_data, get_inventory_data

st.set_page_config(page_title="Sales Analytics | AI Retail Copilot", page_icon="📊", layout="wide")

st.title("📊 Sales Analytics & Business Insights")
st.markdown("Sales trends, KPI dashboards, and profitability analysis.")

sales_df = get_sales_data()
inv_df = get_inventory_data()

st.subheader("Revenue & Trend Performance")

fig_revenue = px.area(sales_df, x='Date', y='Revenue ($)', title="30-Day Revenue Trend", color_discrete_sequence=['#4CAF50'])
st.plotly_chart(fig_revenue, use_container_width=True)

st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Category Performance")
    # Quick mock aggregation since mock data is randomized per execution
    category_counts = inv_df.groupby('Category').size().reset_index(name='Items Count')
    fig_cat = px.pie(category_counts, names='Category', values='Items Count', title="Product Distribution by Category", hole=0.4)
    st.plotly_chart(fig_cat, use_container_width=True)

with col2:
    st.subheader("Product Recommendations (Cross-sell/Upsell)")
    st.info("💡 **AI Recommendation Engine:** Customers who bought **Wireless Earbuds** also frequently bought the **Bluetooth Speaker**.")
    st.warning("💡 **Upsell Opportunity:** Your **Fitness Tracker** customers have a 35% higher LTV (Lifetime Value). Offer a bundle discount with the **Yoga Mat**.")
    st.success("💡 **Pricing Optimization:** Demand for **Smart T-Shirt** is up 20% this week. An A/B test on a 5% price increase is recommended.")

st.markdown("---")
st.subheader("Business Intelligence & Profitability")
st.write("Below is an AI-generated natural language summary of your sales data.")
st.markdown("""
> Based on your 30-day trailing revenue data and current inventory holding costs, your business is operating at an estimated **22% net margin**.
> 
> *   **Strongest Driver:** The **Fitness** category has shown consistent week-over-week growth.
> *   **Drag on Profitability:** You are currently overstocked on **Apparel** items with a slow inventory turnover rate of 1.2. 
> 
> **AI Copilot Recommendation:** Initiate a localized email marketing campaign offering 10% off Apparel to clear stock and improve cash flow.
""")
