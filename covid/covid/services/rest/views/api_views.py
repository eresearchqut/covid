from rdrf.services.rest.views.api_views import PatientDetail
from ..serializers import CovidPatientSerializer


class CovidPatientDetail(PatientDetail):
    serializer_class = CovidPatientSerializer
