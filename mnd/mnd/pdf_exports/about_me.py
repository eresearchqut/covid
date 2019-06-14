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
        'First': patient.given_names,
        'Last': patient.family_name,
        'Maiden name if applicable': patient.maiden_name,
        'DOB': patient.date_of_birth.strftime("%d/%m/%Y") if patient.date_of_birth else '',
        '8 digits': patient.home_phone or '',
        'Mobile Number': patient.mobile_phone or '',
        'Email': patient.email or ''
    }
    patient_address = patient.home_address
    if patient_address:
        data.update({
            'Suburb': patient_address.suburb,
            'Address': patient_address.address,
            'Postcode': patient_address.postcode,
            'State': _STATE_VALUE_MAPPING.get(patient_address.state, 'QLD')
        })

    # TODO
    # dynamic_data = patient.get_dynamic_data(registry)

    return data


def get_pdf_template():
    return f"{PDF_TEMPLATES_PATH}/about_me.pdf"
