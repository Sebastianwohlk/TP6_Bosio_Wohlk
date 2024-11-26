from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, search_patient_by_document
from observation import create_observation_resource
import time

if __name__ == "__main__":
    # Patient parameters
    family_name = "Doe"
    given_name = "John"
    birth_date = "1990-01-01"
    gender = "male"
    phone = None
    document_number = "123456789-unique2"

    # Create and send the patient resource
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, document_number)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    if patient_id:
        print(f"Created Patient ID: {patient_id}")
        created_patient = get_resource_from_hapi_fhir(patient_id, "Patient")

        # Wait for server indexing
        print("Waiting for server to index the new resource...")
        time.sleep(5)

        # Search for the created patient by document number
        print(f"Searching for the created patient by document number ({document_number})...")
        found_patient = search_patient_by_document(document_number, expected_patient_id=patient_id)
        if found_patient:
            print("Found the created patient!")

        # Create an observation for the patient (e.g., temperature)
        observation_code = "8310-5"  # LOINC code for body temperature
        observation_value = 37  # Example temperature value
        observation_unit = "C"  # Unit of measurement (Celcius)

        # Create the Observation resource using patient_id
        observation = create_observation_resource(patient_id, observation_code, observation_value, observation_unit)

        # Send the Observation resource to the HAPI FHIR server
        observation_id = send_resource_to_hapi_fhir(observation, "Observation")
        if observation_id:
            print(f"Observation created successfully with ID: {observation_id}")

    
            # Retrieve the created Observation resource from the server
            created_observation = get_resource_from_hapi_fhir(observation_id, "Observation")




