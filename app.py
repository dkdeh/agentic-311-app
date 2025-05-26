import streamlit as st
import random

# Simulated backend categories and status
categories = ["Pothole", "Trash Pickup", "Noise Complaint", "Streetlight Out", "Water Leak"]
status_options = ["Received", "In Progress", "Resolved", "Escalated"]

st.set_page_config(page_title="Agentic 311 Request System", layout="centered")
st.title("📞 Agentic 311 Request Assistant")

st.markdown("""
Use this assistant to report a city issue. Agentic AI will classify and route your request.
""")

# Input section
with st.form("311_form"):
    user_name = st.text_input("Your Name")
    user_location = st.text_input("Location (Address or Zip Code)")
    user_issue = st.text_area("Describe the issue you're reporting")
    submitted = st.form_submit_button("Submit Request")

if submitted:
    # Simulated classification and response
    issue_type = random.choice(categories)
    ticket_id = f"TKT-{random.randint(1000,9999)}"
    ticket_status = random.choice(status_options)

    st.success(f"Thank you, {user_name}! Your request has been received.")
    st.info(f"🧠 Agent classified this as: **{issue_type}**")
    st.markdown(f"**Tracking ID**: `{ticket_id}`")
    st.markdown(f"**Current Status**: `{ticket_status}`")

    # Simulate AI suggestion or reply
    if issue_type == "Pothole":
        st.markdown("✅ This will be routed to the Streets Department.")
    elif issue_type == "Trash Pickup":
        st.markdown("♻️ This will be handled by the Sanitation Division.")
    elif issue_type == "Noise Complaint":
        st.markdown("🔊 Routed to Local Code Enforcement.")
    elif issue_type == "Streetlight Out":
        st.markdown("💡 Sent to Public Lighting Authority.")
    elif issue_type == "Water Leak":
        st.markdown("🚰 Assigned to the Water Department.")
