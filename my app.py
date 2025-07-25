import streamlit as st
import pandas as pd
from datetime import date

# --- USERS ---
USER_CREDENTIALS = {
    "abdusemed": "1234",
    "mubarik": "9887",
    "welela": "1000"
}

# --- SESSION ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'clinic_data' not in st.session_state:
    st.session_state.clinic_data = []

# --- LOGIN FUNCTION ---
def login():
    st.title("🔐 AL Mubarik Medium Clinic Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")

        if login_btn:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.success(f"✅ Welcome, {username}!")
                st.session_state.logged_in = True
            else:
                st.error("❌ Invalid username or password")

# --- MAIN CLINIC APP ---
def clinic_main():
    st.title("🏥 Doctor Mubarik Medium Clinic")

    st.subheader("📋 Patient Registration Form")
    with st.form("clinic_form"):
        patient_id = st.text_input("Patient ID")
        patient_name = st.text_input("Patient Name")
        history = st.text_area("Medical History")
        physical_exam = st.text_area("Physical Examination")
        cbc = st.text_input("CBC Result")
        chemistry = st.text_input("Chemistry Result")
        total_price = st.number_input("Total Price (in ETB)", min_value=0.0, format="%.2f")
        appointment = st.date_input("Next Appointment Date", value=date.today())
        submit = st.form_submit_button("Save Patient Record")

        if submit:
            st.session_state.clinic_data.append({
                "Patient ID": patient_id,
                "Name": patient_name,
                "History": history,
                "Physical Exam": physical_exam,
                "CBC": cbc,
                "Chemistry": chemistry,
                "Price": total_price,
                "Appointment": appointment.strftime("%Y-%m-%d")
            })
            st.success("✅ Patient record saved.")

    st.subheader("📑 Clinic Records")
    if st.session_state.clinic_data:
        df = pd.DataFrame(st.session_state.clinic_data)
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False)
        st.download_button("⬇️ Download Records", data=csv, file_name="clinic_records.csv", mime="text/csv")
    else:
        st.info("No patient records yet.")

# --- APP CONTROL ---
if not st.session_state.logged_in:
    login()
else:
    clinic_main()
