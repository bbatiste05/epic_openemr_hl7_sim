from flask import Flask, request
import os
os.makedirs("hl7_logs", exist_ok=True)

app = Flask(__name__)

@app.route('/hl7', methods=['POST'])
def receive_hl7():
    hl7_msg = request.data.decode("utf-8")
    print("✅ Received HL7 Message:\n", hl7_msg)

    # Return a basic ACK HL7 response
    ack = "MSH|^~\\&|RECEIVER|HOSP|SENDER|CLINIC|202507210945||ACK|12345|P|2.3\rMSA|AA|12345"
    return ack, 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
