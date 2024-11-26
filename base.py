import requests
from patient import create_patient_resource

BASE_URL = "https://launch.smarthealthit.org/v/r4/fhir"  # Base URL for the SMART FHIR server

# Enviar el recurso FHIR al servidor SMART FHIR
def send_resource_to_hapi_fhir(resource, resource_type):
    url = f"{BASE_URL}/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        return response.json().get('id')
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None


# Buscar el recurso por ID
def get_resource_from_hapi_fhir(resource_id, resource_type):
    url = f"{BASE_URL}/{resource_type}/{resource_id}"
    headers = {"Accept": "application/fhir+json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        resource = response.json()
        print("Resource found:")
        print(resource)
        return resource
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.text)
        return None


# Buscar un paciente por su número de documento
def search_patient_by_document(document_number, expected_patient_id=None):
    url = f"{BASE_URL}/Patient?identifier={document_number}"
    headers = {"Accept": "application/fhir+json"}
    print(f"Search URL: {url}")  # Debugging: Print the search URL

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        results = response.json()

        if "entry" in results:
            print("Patient(s) found:")
            for entry in results["entry"]:
                patient = entry["resource"]
                # Filter by expected ID if provided
                if expected_patient_id and patient.get("id") == expected_patient_id:
                    print("Found the exact patient:")
                    print(patient)
                    return patient
            print("Exact patient not found. Showing all matching patients:")
            for entry in results["entry"]:
                print(entry["resource"])  # Display other matching patients
        else:
            print("No patients found with the given document number.")
            return None
    else:
        print(f"Error searching for patient: {response.status_code}")
        print(response.text)
        return None
