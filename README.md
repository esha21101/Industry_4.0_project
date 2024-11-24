# **Distributed System for Industry 4.0*
A distributed system that integrates Suppliers, OEM Manufacturers, and Retailers to streamline the ordering, assembly, and feedback management processes for machine parts. The system ensures real-time communication, effective data management, and improved customer satisfaction.

# Features
Order Management: Handle machine part orders from suppliers to OEM manufacturers and shipment to retailers.<br>
Feedback System: Allow retailers to submit customer feedback on finished products. Feedback is routed to the supplier for resolving defects and re-shipment.<br>
Integrated Data Model: Maintain a centralized database for tracking machine parts, assembly details, and feedback.<br>
Web Interface: A responsive front end for Suppliers, OEM Manufacturers, and Retailers with dynamic dashboards.
# Tech Stack
# Frontend
Framework: Streamlit<br>
Languages: HTML, CSS, JavaScript (with React.js styles)
# Features:
Dynamic forms for order creation and feedback submission.<br>
Real-time data visualization.<br>
Styled using custom CSS for user-friendly navigation.
# Backend
Framework: Flask<br>
APIs: RESTful APIs for order and feedback management.<br>
Programming Language: Python
# Features:
Endpoint for order management (/orders).<br>
Endpoint for feedback routing (/feedback).<br>
Database<br>
Database System: SQLite<br>
Schema: Centralized schema with tables for orders, feedback, products, and assembly details.<br>
Installation

# Prerequisites
 Python 3.8+<br>
 Flask<br>
 Streamlit<br>
# Setup
Clone the repository:

bash<br>
Copy code
git clone https://github.com/your-username/distributed-system-industry4.0.git  <br>
cd distributed-system-industry4.0  <br>
Create a virtual environment and activate it:<br>

bash<br>
Copy code
python -m venv env  <br>
source env/bin/activate  # On Windows: env\Scripts\activate <br> 
Install dependencies:<br>

bash<br>
Copy code<br>
pip install -r requirements.txt  <br>
Run the backend server:<br>

bash<br>
Copy code<br>
python backend/app.py  <br>
Run the frontend:<br>

bash<br>
Copy code<br>
streamlit run frontend/interface.py<br>  
# Usage
Backend APIs<br>
Order API:<br>

Endpoint: POST /orders<br>
Example Request:<br>
json<br>
Copy code<br>
{  
  "product_id": 123, <br> 
  "quantity": 5,  <br>
  "retailer_id": 10  <br>
}  
Response:<br>
json<br>
Copy code<br>
{  
  "order_id": 456, <br> 
  "status": "success"  <br>
}  
Feedback API:<br>

Endpoint: POST /feedback<br>
Example Request:<br>
json<br>
Copy code<br>
{  
  "product_id": 123,  <br>
  "feedback": "Part defective",  <br>
  "retailer_id": 10  <br>
}  
Response:<br>
json<br>
Copy code<br>
{  
  "feedback_id": 789,  <br>
  "status": "received"  <br>
}  
# Frontend Interface
Suppliers: View and manage part orders.<br>
OEM Manufacturers: Track product assembly and manage supplier communication.<br>
Retailers: Submit feedback and review order details.<br>
# Project Structure
graphql<br>
Copy code<br>
distributed-system-industry4.0/  <br>
│  
├── backend/  
│   ├── app.py                   # Main Flask application  
│   ├── models.py                # Database models  
│   ├── routes/                  # API route definitions  
│   │   ├── order_routes.py  
│   │   ├── feedback_routes.py  
│   ├── database/                # SQLite database  
│       ├── database.db  
│       ├── schema.sql           # Database schema  
│  
├── frontend/  
│   ├── interface.py             # Main Streamlit application  
│   ├── components/              # Frontend components (HTML/CSS templates)  
│  
├── requirements.txt             # Python dependencies  
├── README.md                    # Project documentation  
# Future Enhancements
Integration with cloud databases (e.g., PostgreSQL).<br>
Real-time notifications for feedback updates.<br>
Advanced analytics and reporting dashboards.<br>
# Pull requests are welcome. For major changes, please open an issue to discuss what you would like to change.
