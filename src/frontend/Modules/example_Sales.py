import streamlit as st
from backend.example_sales import get_sales_data, calculate_sales_metrics, get_monthly_sales
# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------
title = "example Sales"
icon = ":material/euro:"

# ---------------------------------------
# PAGE ELEMENTS
# ---------------------------------------
st.title("📈 Sales Dashboard")
st.balloons()

# Get data
sales_data = get_sales_data()
metrics = calculate_sales_metrics(sales_data)

# Display key metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Sales", f"${metrics['total']:,.0f}")
with col2:
    st.metric("Average Sale", f"${metrics['average']:.2f}")
with col3:
    st.metric("Best Month", metrics['best_month'])
with col4:
    st.metric("Growth", f"{metrics['growth']:.1f}%")

# Monthly sales chart
st.subheader("Monthly Sales Trend")
monthly_data = get_monthly_sales(sales_data)
st.line_chart(monthly_data)

# Sales by category
st.subheader("Sales by Category")
category_data = {}
for sale in sales_data:
    category = sale['category']
    if category not in category_data:
        category_data[category] = 0
    category_data[category] += sale['amount']

st.bar_chart(category_data)

# Raw data table
if st.checkbox("Show detailed sales data"):
    st.dataframe(sales_data)