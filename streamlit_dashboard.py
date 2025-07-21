import glob
import os
from datetime import datetime

import streamlit as st

st.set_page_config(page_title="HL7 Message Viewer", layout="wide")

st.title("📥 HL7 Inbound Message Dashboard")

LOG_DIR = "hl7_logs"

# Get all HL7 files
hl7_files = sorted(glob.glob(f"{LOG_DIR}/*.txt"), reverse=True)

# Quick stats
st.metric("📂 Total Messages", len(hl7_files))

# Filter by message type
msg_filter = st.multiselect("📑 Filter by Message Type", ["ADT", "ORU", "SIU"], default=["ADT", "ORU", "SIU"])

# Table structure
parsed_data = []

for file_path in hl7_files:
    with open(file_path, "r") as f:
        content = f.read()

    # Basic parsing
    msg_lines = content.strip().split("\n")
    msh = msg_lines[0].split("|") if msg_lines else []
    pid = next((line.split("|") for line in msg_lines if line.startswith("PID")), None)

    msg_type = msh[8] if len(msh) > 8 else "UNKNOWN"
    timestamp = msh[6] if len(msh) > 6 else "UNKNOWN"
    patient_id = pid[3] if pid and len(pid) > 3 else "?"
    name = pid[5] if pid and len(pid) > 5 else "?"

    if msg_type.split("^")[0] in msg_filter:
        parsed_data.append({
            "Filename": os.path.basename(file_path),
            "Type": msg_type,
            "Patient ID": patient_id,
            "Name": name.replace("^", " "),
            "Timestamp": timestamp,
            "Full Message": content
        })

# Table
if parsed_data:
    st.subheader("📄 Parsed HL7 Messages")
    st.dataframe(parsed_data, use_container_width=True)

    # Select to view raw message
    selected_file = st.selectbox("🔎 Select a message to view full content", [d["Filename"] for d in parsed_data])
    full_msg = next((d["Full Message"] for d in parsed_data if d["Filename"] == selected_file), "")

    st.text_area("📜 Full HL7 Message", full_msg, height=300)
else:
    st.info("No HL7 messages found or matching selected filters.")

import pandas as pd

# Show table
df = pd.DataFrame(parsed_data)
st.dataframe(df.drop(columns=["Full Message"]), use_container_width=True)

# Export button
csv = df.to_csv(index=False)
st.download_button("📥 Download as CSV", csv, file_name="hl7_messages.csv", mime="text/csv")
