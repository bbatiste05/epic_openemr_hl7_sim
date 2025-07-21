# 🏥 Epic to OpenEMR HL7 Simulation Lab

This project simulates a real-world HL7 workflow between an EHR system like Epic and an OpenEMR-like receiver. It includes:

- ✅ HL7 Message Generator (Streamlit)
- ✅ Flask-based HL7 Receiver
- ✅ Streamlit HL7 Dashboard for viewing + exporting messages

> Built as part of a hands-on healthcare IT integration portfolio using Python, Flask, and Streamlit.

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


