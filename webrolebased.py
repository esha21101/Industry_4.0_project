import streamlit as st
import pandas as pd
from datetime import datetime

# Set page config for layout and favicon
st.set_page_config(
    page_title="RepairNet",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS for colorful and smooth design
def add_custom_css():
    st.markdown(
        """
        <style>
        /* Set vibrant background */
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            font-family: "Arial", sans-serif;
        }

        /* Style buttons */
        .stButton > button {
            background: linear-gradient(90deg, #6a11cb, #2575fc);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 8px 20px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #2575fc, #6a11cb);
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
        }

        /* Sidebar styling */
        .css-1d391kg {
            background: linear-gradient(180deg, #3a6186, #89253e);
            color: white;
            padding: 10px;
            border-radius: 10px;
        }

        /* Style dataframe */
        .stDataFrame {
            background: white;
            border-radius: 8px;
            padding: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }

        /* Header styling */
        .header-style {
            color: #ffffff;
            text-align: center;
            background: rgba(0, 0, 0, 0.2);
            padding: 10px;
            border-radius: 10px;
        }

        /* Form styling */
        .stForm {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


add_custom_css()

# Initialize session state data
if "orders" not in st.session_state:
    st.session_state.orders = []
if "feedback" not in st.session_state:
    st.session_state.feedback = []
if "role" not in st.session_state:
    st.session_state.role = None

# Role Selection
if st.session_state.role is None:
    st.markdown('<h1 class="header-style">🔧 Welcome to RepairNet 🔧</h1>', unsafe_allow_html=True)
    st.markdown("### Select your role to get started:")
    role = st.selectbox(
        "Select Role", ["Supplier", "Manufacturer", "Retailer"], key="role_select"
    )
    if st.button("Confirm Role", key="confirm_role"):
        st.session_state.role = role
        st.experimental_rerun()

# Supplier Interface
elif st.session_state.role == "Supplier":
    st.sidebar.title("💼 Supplier Dashboard")
    page = st.sidebar.radio("📌 Navigate", ["Home", "Manage Orders"])

    if page == "Home":
        st.markdown('<h1 class="header-style">Welcome, Supplier!</h1>', unsafe_allow_html=True)
        st.markdown("🔍 **View and manage orders placed by manufacturers.**")

    elif page == "Manage Orders":
        st.markdown('<h1 class="header-style">📦 Manage Orders</h1>', unsafe_allow_html=True)
        if st.session_state.orders:
            supplier_orders = [
                order for order in st.session_state.orders if order["Status"] == "Ordered"
            ]
            if supplier_orders:
                st.dataframe(pd.DataFrame(supplier_orders))
                st.markdown("### 🚚 Mark orders as shipped:")
                selected_order = st.selectbox(
                    "Select an Order to Mark as Shipped",
                    [order["Part Name"] for order in supplier_orders],
                )
                if st.button("Mark as Shipped"):
                    for order in st.session_state.orders:
                        if order["Part Name"] == selected_order:
                            order["Status"] = "Shipped"
                    st.success(f"✅ {selected_order} marked as shipped.")
            else:
                st.write("❌ No orders to process.")
        else:
            st.write("❌ No orders placed yet.")

# Manufacturer Interface
elif st.session_state.role == "Manufacturer":
    st.sidebar.title("🏭 Manufacturer Dashboard")
    page = st.sidebar.radio(
        "📌 Navigate", ["Home", "Order Machine Part", "Assemble Product"]
    )

    if page == "Home":
        st.markdown('<h1 class="header-style">Welcome, Manufacturer!</h1>', unsafe_allow_html=True)
        st.markdown("🔍 **Order parts and manage assemblies here.**")

    elif page == "Order Machine Part":
        st.markdown('<h1 class="header-style">🛠️ Order Machine Part</h1>', unsafe_allow_html=True)
        with st.form("order_form"):
            st.markdown("### 📋 Fill in the order details:")
            part_name = st.text_input("Machine Part Name", value="Gear Assembly")
            supplier_name = st.selectbox(
                "Supplier", ["Supplier A", "Supplier B", "Supplier C"]
            )
            quantity = st.number_input("Quantity", min_value=1, value=1)
            order_date = st.date_input("Order Date", value=datetime.now().date())
            submit_order = st.form_submit_button("📦 Place Order")

            if submit_order:
                st.session_state.orders.append(
                    {
                        "Part Name": part_name,
                        "Supplier": supplier_name,
                        "Quantity": quantity,
                        "Order Date": order_date,
                        "Status": "Ordered",
                    }
                )
                st.success(
                    f"✅ Order placed for {quantity} units of {part_name} from {supplier_name}."
                )

    elif page == "Assemble Product":
        st.markdown('<h1 class="header-style">🔧 Assembly Process</h1>', unsafe_allow_html=True)
        if st.session_state.orders:
            shipped_orders = [
                order for order in st.session_state.orders if order["Status"] == "Shipped"
            ]
            if shipped_orders:
                st.markdown("### 🚀 Select a shipped order for assembly:")
                selected_order = st.selectbox(
                    "Select an Order for Assembly",
                    [order["Part Name"] for order in shipped_orders],
                )
                if st.button("Mark as Assembled"):
                    for order in st.session_state.orders:
                        if order["Part Name"] == selected_order:
                            order["Status"] = "Assembled"
                    st.success(f"✅ {selected_order} marked as assembled.")
            else:
                st.write("❌ No shipped orders available for assembly.")
        else:
            st.write("❌ No orders placed yet.")

# Retailer Interface
elif st.session_state.role == "Retailer":
    st.sidebar.title("🛍️ Retailer Dashboard")
    page = st.sidebar.radio("📌 Navigate", ["Home", "Customer Feedback", "Reports"])

    if page == "Home":
        st.markdown('<h1 class="header-style">Welcome, Retailer!</h1>', unsafe_allow_html=True)
        st.markdown("🔍 **Manage customer feedback and view reports.**")

    elif page == "Customer Feedback":
        st.markdown('<h1 class="header-style">📝 Customer Feedback</h1>', unsafe_allow_html=True)
        with st.form("feedback_form"):
            st.markdown("### 📋 Submit customer feedback:")
            product_name = st.text_input("Product Name", value="Finished Product")
            customer_name = st.text_input("Customer Name")
            feedback_text = st.text_area("Feedback")
            feedback_date = st.date_input("Feedback Date", value=datetime.now().date())
            submit_feedback = st.form_submit_button("📨 Submit Feedback")

            if submit_feedback:
                st.session_state.feedback.append(
                    {
                        "Product Name": product_name,
                        "Customer Name": customer_name,
                        "Feedback": feedback_text,
                        "Date": feedback_date,
                    }
                )
                st.success("✅ Feedback submitted successfully!")

    elif page == "Reports":
        st.markdown('<h1 class="header-style">📊 Reports</h1>', unsafe_allow_html=True)
        st.markdown("### 🗒️ Feedback Report")
        if st.session_state.feedback:
            st.dataframe(pd.DataFrame(st.session_state.feedback))
        else:
            st.write("❌ No feedback available.")

# Logout Button
if st.sidebar.button("Logout"):
    st.session_state.role = None
    st.experimental_rerun()
