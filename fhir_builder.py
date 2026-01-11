import json
import datetime
import uuid

def create_fhir_patient(first_name, last_name, birth_date, gender, phone):
    """
    Converts raw patient data into a Standard HL7 FHIR R4 Resource.
    This is required for integration with Epic, Cerner, and Apple Health.
    """
    
    fhir_resource = {
        "resourceType": "Patient",
        "id": str(uuid.uuid4()),
        "meta": {
            "versionId": "1",
            "lastUpdated": datetime.datetime.now().isoformat()
        },
        "text": {
            "status": "generated",
            "div": f"<div xmlns=\"http://www.w3.org/1999/xhtml\">Patient: {first_name} {last_name}</div>"
        },
        "active": True,
        "name": [
            {
                "use": "official",
                "family": last_name,
                "given": [first_name]
            }
        ],
        "telecom": [
            {
                "system": "phone",
                "value": phone,
                "use": "mobile"
            }
        ],
        "gender": gender,
        "birthDate": birth_date
    }
    
    return fhir_resource

# --- Simulating an Incoming Hospital Data Stream ---
incoming_patient = {
    "first": "Sarah",
    "last": "Connor",
    "dob": "1985-04-20",
    "sex": "female",
    "contact": "+1-555-0199"
}

# Convert to FHIR Standard
fhir_output = create_fhir_patient(
    incoming_patient["first"],
    incoming_patient["last"],
    incoming_patient["dob"],
    incoming_patient["sex"],
    incoming_patient["contact"]
)

# Print the result (This creates the JSON that EMRs read)
print(json.dumps(fhir_output, indent=4))
