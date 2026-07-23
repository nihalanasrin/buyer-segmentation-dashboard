import streamlit as st
st.set_page_config(
    page_title="Buyer Segmentation Dashboard",
    page_icon="🏠",
    layout="wide"
)
import pandas as pd

clients = pd.read_csv("data/clients.csv")
st.sidebar.title("🔍 Filters")

country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(clients["country"].unique().tolist())
)
search_name = st.sidebar.text_input("🔍 Search Customer Name")

if country != "All":
    filtered_clients = clients[clients["country"] == country]
else:
    filtered_clients = clients

if search_name:
    filtered_clients = filtered_clients[
        filtered_clients["first_name"].str.contains(search_name, case=False, na=False)
    ]
total_customers = len(filtered_clients)
total_countries = filtered_clients["country"].nunique()
loan_applied = (filtered_clients["loan_applied"] == "Yes").sum()
avg_satisfaction = filtered_clients["satisfaction_score"].mean()
country_count = filtered_clients["country"].value_counts()
country_satisfaction = filtered_clients.groupby("country")["satisfaction_score"].mean()
loan_country = filtered_clients[
    filtered_clients["loan_applied"] == "Yes"
]["country"].value_counts()

st.title("🏠 Buyer Segmentation Dashboard")

st.write("### Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Customers", total_customers)
col2.metric("🌍 Countries", total_countries)
col3.metric("💳 Loans", loan_applied)
col4.metric("⭐ Satisfaction", round(avg_satisfaction, 2))

st.success("🎉 Dashboard Connected Successfully!")
st.subheader("🌍 Customers by Country")

st.bar_chart(country_count)

st.subheader("First 5 Customers")

st.dataframe(filtered_clients.head())
st.subheader("👥 Customers by Type")

customer_type = filtered_clients["client_type"].value_counts()

st.bar_chart(customer_type)
st.subheader("⭐ Average Satisfaction by Country")

st.bar_chart(country_satisfaction)
st.subheader("💳 Loan Applications by Country")

st.bar_chart(loan_country)
referral_count = filtered_clients["referral_channel"].value_counts()

st.subheader("📢 Customers by Referral Channel")

st.bar_chart(referral_count)
st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_clients.to_csv(index=False),
    file_name="filtered_customers.csv",
    mime="text/csv"
)
st.markdown("---")
st.caption("Buyer Segmentation Dashboard | Built using Python, Pandas & Streamlit")