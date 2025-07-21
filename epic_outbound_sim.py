import requests

hl7_message = """
MSH|^~\\&|Epic|Hospital|OpenEMR|Clinic|202507211100||ADT^A01|MSGID12345|P|2.3
PID|1||789123^^^HOSP^MR||Smith^Jane||19751225|F||2106-3|321 Elm St^^Austin^TX^78701||555-9876
PV1|1|I|WARD1^101^1^A^^||||1234^Doe^John||||||||||123456
"""

response = requests.post(
    "http://localhost:5050/hl7",
    headers={"Content-Type": "text/plain"},
    data=hl7_message.strip()
)

print("✅ Epic HL7 Sent")
print("🔁 ACK Response:")
print(response.text)
