import streamlit as st
import plotly.express as px
from utils.mock_data import get_inventory_data

st.set_page_config(page_title="Inventory | AI Retail Copilot", page_icon="📦", layout="wide")

st.title("📦 Inventory Management")
st.markdown("Real-time stock monitoring, reorder alerts, & demand forecasting.")

inv_df = get_inventory_data()

# Summary
low_stock_df = inv_df[inv_df['Status'] == 'Low Stock']

if not low_stock_df.empty:
    st.error(f"⚠️ {len(low_stock_df)} items are currently running low on stock!")
else:
    st.success("✅ All items are healthy and above reorder levels.")

# Data Table
st.subheader("Current Inventory Levels")
st.dataframe(inv_df.style.applymap(lambda x: 'color: red' if x == 'Low Stock' else 'color: green', subset=['Status']), use_container_width=True)

# AI Replenishment Suggestions
st.markdown("---")
st.subheader("🤖 AI Automated Replenishment Suggestions")

if not low_stock_df.empty:
    for index, row in low_stock_df.iterrows():
        suggestion_qty = row['Demand Forecast (Next 30 Days)'] * 1.5 - row['Current Stock']
        with st.expander(f"Restock Suggested: {row['Product']}"):
            st.write(f"**Current Stock:** {row['Current Stock']} (Reorder Level: {row['Reorder Level']})")
            st.write(f"**Generated Demand Forecast (30 Days):** {row['Demand Forecast (Next 30 Days)']} units")
            st.write(f"👉 **Copilot Suggests:** Order **{int(suggestion_qty)}** units within the next 48 hours to prevent stockouts.")
            st.button(f"Generate Purchase Order for {row['Product']}", key=f"btn_{index}")
else:
    st.info("No immediate restock suggestions based on current demand forecasts.")

# Forecasting Chart
st.markdown("---")
st.subheader("Demand Forecasting Visualization")
fig = px.scatter(inv_df, x='Current Stock', y='Demand Forecast (Next 30 Days)', size='Reorder Level', color='Category', hover_name='Product', title="Stock vs Expected Demand")
st.plotly_chart(fig, use_container_width=True)
