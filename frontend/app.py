import streamlit as st
import requests

# Styling
st.set_page_config(layout="wide", page_title="Distributed System Dashboard")
st.markdown('<link rel="stylesheet" href="static/styles.css">', unsafe_allow_html=True)

# Navigation
menu = st.sidebar.selectbox("Navigation", ["Supplier", "Manufacturer", "Retailer"])

if menu == "Supplier":
    st.title("Supplier Dashboard")
    st.subheader("Orders")
    response = requests.get("http://127.0.0.1:5000/api/orders")
    orders = response.json()
    for order in orders:
        st.write(order)

elif menu == "Manufacturer":
    st.title("Manufacturer Dashboard")
    st.subheader("Parts Inventory")
    st.write("View and manage parts here.")

elif menu == "Retailer":
    st.title("Retailer Dashboard")
    st.subheader("Feedback")
    feedback = st.text_area("Enter Customer Feedback")
    if st.button("Submit"):
        response = requests.post("http://127.0.0.1:5000/api/feedback", json={"feedback": feedback})
        st.success("Feedback submitted successfully!")
