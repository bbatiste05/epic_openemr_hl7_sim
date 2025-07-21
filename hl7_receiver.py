import os
from datetime import datetime

from flask import Flask, request

app = Flask(__name__)

# Ensure the log directory exists
LOG_DIR = "hl7_logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.route("/hl7", methods=["POST"])
def receive_hl7():
    hl7_msg = request.data.decode("utf-8")
    
    print("📥 Received HL7 Message:\n", hl7_msg)
    
    # Save HL7 message to a timestamped file
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = os.path.join(LOG_DIR, f"hl7_{timestamp}.txt")
    with open(filename, "w") as f:
        f.write(hl7_msg)
    
    # Return basic ACK (simulate Epic-style response)
    ack_response = f"""MSH|^~\\&|OpenEMR|Listener|Epic|Sender|{timestamp}||ACK|{timestamp}|P|2.3
MSA|AA|{timestamp}"""
    
    return ack_response, 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(port=5050)
