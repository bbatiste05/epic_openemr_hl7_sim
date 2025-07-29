👋 About Me

I'm Brandon Batiste, a healthcare technology analyst with hands-on experience in Epic workflow simulation, infrastructure support, and EMR optimization. This project reflects my commitment to continuous learning and real-world application.

Even without direct Epic access, I built my own sandbox to think like an analyst.

# 🏥 Epic Analyst Simulation: OpenEMR + HL7 + Streamlit

This project simulates key Epic workflows using **OpenEMR**, HL7 messaging, and a custom **Streamlit dashboard** to analyze and visualize clinical and billing data.

---

## 📌 Project Overview

**Goal**: Emulate core Epic modules and workflows—such as Beaker (Lab), Resolute Billing, and In Basket communication—through open tools and demonstrate foundational analyst readiness for Epic support roles.

---

## ⚙️ Tools & Technologies
- [OpenEMR Demo](https://demo.open-emr.org)
- HL7 v2.5.1 Message Simulation
- Streamlit for Dashboard Visualization
- Python (Flask) for HL7 receiver

---

## 🔧 Project Structure
epic_openemr_hl7_sim/
├── epic_outbound_sim.py # HL7 sender GUI (Streamlit)
├── hl7_receiver.py # Flask-based HL7 endpoint
├── streamlit_dashboard.py # HL7 message viewer
├── sample_messages/ # ADT/ORU/SIU examples
├── hl7_logs/ # Inbound HL7 logs (auto-generated)
├── requirements.txt
└── README.md


---
## 🧪 Simulated Workflows

### ✅ Patient Registration  
- Created a new patient `John Doe` via OpenEMR interface  
- Equivalent to: `ADT A04` message in Epic (Patient Add)

### ✅ Clinical Encounter + SOAP Note  
- Entered a full SOAP note during encounter  
- Epic Parallel: SmartText/SmartPhrase documentation

### ✅ Lab Order (CBC Test)  
- Placed order for CBC test via Procedure module  
- Sent as simulated `ORM^O01` HL7 message

### ✅ Lab Result Entry  
- Result manually entered and saved  
- Sent as outbound `ORU^R01` HL7 message to Flask receiver

### ✅ In Basket Message Simulation  
- Used internal messaging to simulate follow-up note to provider  
- Mimics Epic’s In Basket communication for clinical collaboration

### ✅ Billing Claim (HCFA 1500)  
- Generated and reviewed billing claims  
- Simulates Resolute Professional Billing (PB) workflow

### ✅ Modifier Entry for CPT Code  
- Manually added Modifier `-25` to simulate denial prevention  
- Epic Parallel: Charge Router → Claim Edit Rules

---

## 📊 Streamlit Dashboard

| Feature | Description |
|--------|-------------|
| ✅ HL7 Log Viewer | Displays inbound ORU messages |
| ✅ Error Detector | Highlights malformed messages |
| ✅ Patient Tracker | Tracks simulated patient workflows |
| ✅ CSV Export | For review or QA submission |

## 🚀 How to Run

### 1️⃣ Start HL7 Receiver

```bash
python3 hl7_receiver.py
```

Listens on http://localhost:5050/hl7 and stores messages in hl7_logs/.

Launch HL7 Sender:
streamlit run epic_outbound_sim.py

Launch HL7 Sender:
streamlit run epic_outbound_sim.py

	•	Select an HL7 message
	•	Send to the receiver
	•	Verify ACK response

View Inbound Messages:
streamlit run streamlit_dashboard.py

📁 Sample HL7 Messages

Available in sample_messages/:

adt_a01.hl7 – Admit
oru_r01.hl7 – Lab result
siu_s12.hl7 – Appointment
ack.hl7 – Acknowledgment
error.hl7 – Simulated application error

🔍 Why This Project Matters

HL7 messaging is the backbone of clinical interoperability. This project shows your ability to:

Simulate EHR integration workflows
Parse and display HL7 logs
Build clinical dashboards for visibility and compliance
Use Python + Streamlit in real healthcare scenarios

👨‍⚕️ Built With

Python 3.x
Flask
Streamlit
Pandas
HL7 V2.x knowledge


