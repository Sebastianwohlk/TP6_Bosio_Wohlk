from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    family_name = "Doe"
    given_name = "John"
    birth_date = "1990-01-01"
    gender = "male"
    phone = None 
    document_number = "123456789"

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, document_number)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    # Ver el recurso de paciente creado
    if patient_id:
        get_resource_from_hapi_fhir(patient_id,'Patient')