from rdrf.forms.registration_forms import PatientRegistrationForm


class CovidRegistrationForm(PatientRegistrationForm):
    phone_number = None
