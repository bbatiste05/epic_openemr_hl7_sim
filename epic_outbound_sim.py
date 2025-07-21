import streamlit as st
import requests
from datetime import datetime
import random

st.set_page_config(page_title="Epic HL7 Sender", layout="centered")

st.title("📤 Epic HL7 Message Simulator")

# ---------------------
# 1. User Inputs
# ---------------------
msg_type = st.selectbox("Select HL7 Message Type", ["ADT^A01", "ORU^R01", "SIU^S12"])
patient_id = st.text_input("Patient ID", "123456")
first_name = st.text_input("First Name", "Jane")
last_name = st.text_input("Last Name", "Smith")
dob = st.date_input("Date of Birth")
gender = st.selectbox("Gender", ["F", "M", "O"])
provider = st.text_input("Ordering Provider", "Doe^John")

# ---------------------
# 2. Generate HL7
# ---------------------
now = datetime.now()
ts = now.strftime("%Y%m%d%H%M%S")
msg_id = f"MSG{random.randint(10000,99999)}"

if msg_type == "ADT^A01":
    hl7 = f"""MSH|^~\\&|Epic|Hospital|OpenEMR|Clinic|{ts}||ADT^A01|{msg_id}|P|2.3
PID|1||{patient_id}^^^HOSP^MR||{last_name}^{first_name}||{dob.strftime('%Y%m%d')}|{gender}||2106-3|123 Main St^^City^ST^77001||555-1234
PV1|1|I|WARD1^101^1^A^^||||1234^{provider}||||||||||{random.randint(100000,999999)}"""
elif msg_type == "ORU^R01":
    hl7 = f"""MSH|^~\\&|Epic|Hospital|OpenEMR|Clinic|{ts}||ORU^R01|{msg_id}|P|2.3
PID|1||{patient_id}^^^HOSP^MR||{last_name}^{first_name}||{dob.strftime('%Y%m%d')}|{gender}
OBR|1||LAB54321|88304^Biopsy^CPT||{ts}
OBX|1|NM|8480-6^Systolic BP^LN||130|mmHg|90-140|N|||F"""
elif msg_type == "SIU^S12":
    hl7 = f"""MSH|^~\\&|Epic|Hospital|OpenEMR|Clinic|{ts}||SIU^S12|{msg_id}|P|2.3
SCH|1234|APPT{patient_id}|ClinicVisit|15|min|{ts}|{ts}|||{provider}
PID|1||{patient_id}^^^HOSP^MR||{last_name}^{first_name}||{dob.strftime('%Y%m%d')}|{gender}"""

st.subheader("📄 Generated HL7 Message")
st.code(hl7, language="text")

# ---------------------
# 3. Send Button
# ---------------------
if st.button("📨 Send HL7 Message"):
    try:
        response = requests.post(
            "http://localhost:5050/hl7",
            headers={"Content-Type": "text/plain"},
            data=hl7
        )
        st.success("✅ Message sent successfully!")
        st.code(response.text, language="text")
    except Exception as e:
        st.error(f"❌ Error sending message: {e}")
