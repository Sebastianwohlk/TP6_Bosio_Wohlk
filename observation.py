from fhir.resources.observation import Observation
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference
from fhir.resources.quantity import Quantity
from datetime import datetime

def create_observation_resource(patient_id, observation_code, observation_value, observation_unit):
    # Define the Observation resource
    observation = Observation.construct(
        resourceType="Observation",
        status="final",
        category=[{
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "vital-signs",
                    "display": "Vital Signs"
                }
            ]
        }],
        code=CodeableConcept.construct(
            coding=[Coding.construct(
                system="http://loinc.org",
                code=observation_code,
                display="Body temperature"
            )]
        ),
        subject=Reference.construct(
            reference=f"Patient/{patient_id}"
        ),
        effectiveDateTime=datetime.now().isoformat(),
        valueQuantity=Quantity.construct(
            value=observation_value,
            unit=observation_unit,
            system="http://unitsofmeasure.org",
            code=observation_unit
        )
    )

    return observation

    
