import streamlit as st
import pandas as pd
import plotly.express as px
from utils.mock_data import get_sales_data, get_inventory_data

st.set_page_config(page_title="Dashboard | AI Retail Copilot", page_icon="📈", layout="wide")

st.title("📈 Business Dashboard")
st.markdown("Real-time summary of your retail operations.")

# Fetch data
sales_df = get_sales_data()
inv_df = get_inventory_data()

# Calculate KPIs
total_revenue = sales_df['Revenue ($)'].sum()
avg_daily_revenue = sales_df['Revenue ($)'].mean()
low_stock_items = len(inv_df[inv_df['Status'] == 'Low Stock'])
total_units_sold = sales_df['Daily Units Sold'].sum()

# Display KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue (30 days)", f"${total_revenue:,.2f}")
col2.metric("Avg Daily Revenue", f"${avg_daily_revenue:,.2f}")
col3.metric("Units Sold", f"{total_units_sold:,}")
col4.metric("Low Stock Alerts", f"{low_stock_items}", delta="-"+str(low_stock_items), delta_color="inverse")

st.markdown("---")

# Visualizations
st.subheader("Sales Trend & Forecasting")
fig_sales = px.line(sales_df, x='Date', y='Revenue ($)', title="30-Day Revenue Trend", markers=True)
st.plotly_chart(fig_sales, use_container_width=True)

st.subheader("Inventory Health Overview")
fig_inv = px.bar(inv_df, x='Product', y=['Current Stock', 'Reorder Level'], barmode='group', title="Current Stock vs Reorder Level")
st.plotly_chart(fig_inv, use_container_width=True)

# Copilot Insight
st.info("💡 **Copilot Insight**: Revenue is trending upwards. However, you have several items hitting their reorder level soon. Head to the Inventory page for automated replenishment suggestions.")
