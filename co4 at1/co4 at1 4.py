sentences = {
    "Doctor prescribed medicine to patient.": {
        "Subject": "Doctor",
        "Verb": "prescribed",
        "Object": "Medicine",
        "Role": "Doctor -> Agent, Medicine -> Theme, Patient -> Recipient"
    },

    "Patient reported severe headache.": {
        "Subject": "Patient",
        "Verb": "reported",
        "Object": "Headache",
        "Role": "Patient -> Experiencer, Headache -> Symptom"
    },

    "Nurse monitored patient continuously.": {
        "Subject": "Nurse",
        "Verb": "monitored",
        "Object": "Patient",
        "Role": "Nurse -> Agent, Patient -> Object"
    },

    "Medicine reduced blood pressure.": {
        "Subject": "Medicine",
        "Verb": "reduced",
        "Object": "Blood Pressure",
        "Role": "Medicine -> Cause, Blood Pressure -> Affected Entity"
    }
}

for sentence, data in sentences.items():
    print("Sentence:", sentence)
    print("Subject:", data["Subject"])
    print("Verb:", data["Verb"])
    print("Object:", data["Object"])
    print("Semantic Roles:", data["Role"])
    print("-" * 50)