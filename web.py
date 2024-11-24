import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize data
if "orders" not in st.session_state:
    st.session_state.orders = []
if "feedback" not in st.session_state:
    st.session_state.feedback = []

# Sidebar navigation
st.sidebar.title("Distributed System Simulation")
page = st.sidebar.radio("Navigate", ["Home", "Order Machine Part", "Assembly", "Feedback Management", "Reports"])

# Home Page
if page == "Home":
    st.title("Distributed System Simulation")
    st.markdown("""
        This application simulates the lifecycle of a machine part in a distributed system:
        - **Suppliers** provide machine parts.
        - **OEM Manufacturers** assemble parts into finished products.
        - **Retailers** sell products and manage customer feedback.
        
        Use the sidebar to navigate through processes.
    """)

# Order Machine Part
elif page == "Order Machine Part":
    st.title("Order Machine Part")
    st.markdown("Fill in the details below to order a machine part.")

    with st.form("order_form"):
        part_name = st.text_input("Machine Part Name", value="Gear Assembly")
        supplier_name = st.selectbox("Supplier", ["Supplier A", "Supplier B", "Supplier C"])
        quantity = st.number_input("Quantity", min_value=1, value=1)
        order_date = st.date_input("Order Date", value=datetime.now().date())
        submit_order = st.form_submit_button("Place Order")

        if submit_order:
            st.session_state.orders.append({
                "Part Name": part_name,
                "Supplier": supplier_name,
                "Quantity": quantity,
                "Order Date": order_date,
                "Status": "Ordered"
            })
            st.success(f"Order placed for {quantity} units of {part_name} from {supplier_name}.")

    st.markdown("### Current Orders")
    if st.session_state.orders:
        st.dataframe(pd.DataFrame(st.session_state.orders))
    else:
        st.write("No orders placed yet.")

# Assembly
elif page == "Assembly":
    st.title("Assembly Process")
    st.markdown("Simulate the assembly of machine parts into finished products.")

    if st.session_state.orders:
        order_df = pd.DataFrame(st.session_state.orders)
        selected_order = st.selectbox("Select an Order for Assembly", order_df["Part Name"])
        st.write(f"Assembling: {selected_order}")
        if st.button("Mark as Assembled"):
            for order in st.session_state.orders:
                if order["Part Name"] == selected_order:
                    order["Status"] = "Assembled"
            st.success(f"{selected_order} marked as Assembled.")
    else:
        st.write("No orders available for assembly.")

# Feedback Management
elif page == "Feedback Management":
    st.title("Feedback Management")
    st.markdown("Submit and track feedback for finished products.")

    with st.form("feedback_form"):
        product_name = st.text_input("Product Name", value="Finished Product")
        customer_name = st.text_input("Customer Name")
        feedback_text = st.text_area("Feedback")
        feedback_date = st.date_input("Feedback Date", value=datetime.now().date())
        submit_feedback = st.form_submit_button("Submit Feedback")

        if submit_feedback:
            st.session_state.feedback.append({
                "Product Name": product_name,
                "Customer Name": customer_name,
                "Feedback": feedback_text,
                "Date": feedback_date
            })
            st.success("Feedback submitted successfully!")

    st.markdown("### Submitted Feedback")
    if st.session_state.feedback:
        st.dataframe(pd.DataFrame(st.session_state.feedback))
    else:
        st.write("No feedback submitted yet.")

# Reports
elif page == "Reports":
    st.title("Reports")
    st.markdown("View consolidated reports for orders, assemblies, and feedback.")

    st.markdown("### Order Report")
    if st.session_state.orders:
        st.dataframe(pd.DataFrame(st.session_state.orders))
    else:
        st.write("No orders available.")

    st.markdown("### Feedback Report")
    if st.session_state.feedback:
        st.dataframe(pd.DataFrame(st.session_state.feedback))
    else:
        st.write("No feedback available.")
