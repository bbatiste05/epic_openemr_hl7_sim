import glob
import os

import pandas as pd
import streamlit as st

st.set_page_config(page_title="HL7 Viewer", layout="wide")
st.title("📥 HL7 Inbound Message Dashboard")

LOG_DIR = "hl7_logs"
hl7_files = sorted(glob.glob(f"{LOG_DIR}/*.txt"), reverse=True)

# Filter options
msg_filter = st.multiselect("Filter by Message Type", ["ADT", "ORU", "SIU"], default=["ADT", "ORU", "SIU"])

parsed_data = []

for file in hl7_files:
    with open(file, "r") as f:
        content = f.read()

    lines = content.split("\n")
    msh = next((line for line in lines if line.startswith("MSH")), None)
    pid = next((line for line in lines if line.startswith("PID")), None)

    if msh:
        msh_fields = msh.split("|")
        msg_type = msh_fields[8] if len(msh_fields) > 8 else "UNKNOWN"
        timestamp = msh_fields[6] if len(msh_fields) > 6 else "UNKNOWN"
    else:
        msg_type = "UNKNOWN"
        timestamp = "UNKNOWN"

    if pid:
        pid_fields = pid.split("|")
        patient_id = pid_fields[3] if len(pid_fields) > 3 else "?"
        name = pid_fields[5].replace("^", " ") if len(pid_fields) > 5 else "?"
    else:
        patient_id = "?"
        name = "?"

    if msg_type.split("^")[0] in msg_filter:
        parsed_data.append({
            "Filename": os.path.basename(file),
            "Type": msg_type,
            "Patient ID": patient_id,
            "Name": name,
            "Timestamp": timestamp,
            "Full Message": content
        })

# Display table
if parsed_data:
    df = pd.DataFrame(parsed_data)
    st.dataframe(df.drop(columns=["Full Message"]), use_container_width=True)

    # Export to CSV
    csv = df.to_csv(index=False)
    st.download_button("📥 Download CSV", csv, "hl7_messages.csv")

    # Select raw message
    selected_file = st.selectbox("View HL7 Message", df["Filename"])
    full_msg = df[df["Filename"] == selected_file]["Full Message"].values[0]
    st.text_area("📜 Full HL7 Message", full_msg, height=300)
else:
    st.warning("No HL7 messages found or matching selected types.")

