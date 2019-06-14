from ..settings import PDF_TEMPLATES_PATH

_STATE_VALUE_MAPPING = {
    'AU-SA': 'SA',
    'AU-ACT': 'ACT',
    'AU-NT': 'NT',
    'AU-TAS': 'TAS',
    'AU-QLD': 'QLD',
    'AU-WA': 'WA',
    'AU-VIC': 'VIC'
}


def generate_pdf_form_fields(registry, patient):
    data = {
        'pFirstName': patient.given_names,
        'pLastName': patient.family_name,
        'pMaidenName': patient.maiden_name,
        'pDOB': patient.date_of_birth.strftime("%d/%m/%Y") if patient.date_of_birth else '',
        'pPhoneNo': patient.home_phone,
        'pMobile': patient.mobile_phone,
        'pEmail': patient.email,
    }
    patient_address = patient.home_address
    if patient_address:
        data.update({
            'pSuburb': patient_address.suburb,
            'pAddress': patient_address.address,
            'pPostcode': patient_address.postcode,
            'pState': _STATE_VALUE_MAPPING.get(patient_address.state, 'QLD') if patient_address.state else '',
        })

    # TODO
    # dynamic_data = patient.get_dynamic_data(registry)

    return {k: '' if v is None else v for k, v in data.items()}


def get_pdf_template():
    return f"{PDF_TEMPLATES_PATH}/About me and MND_Interactive_v2.pdf"
