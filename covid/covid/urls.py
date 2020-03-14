from django.conf.urls import include
from django.urls import re_path

from .views.covid_patient_view import AddPatientView, PatientEditView
from .views.covid_patients_listing import CovidPatientListingView
from rdrf.urls import urlpatterns as rdrf_urlpatterns

rdrf_urls = [p for p in rdrf_urlpatterns if not getattr(p, 'app_name', None) == 'api_urls']

urlpatterns = [
    # Any custom URLs go here before we include the TRRF urls
    re_path(r"^(?P<registry_code>\w+)/patient/add/?$", AddPatientView.as_view(), name='patient_add'),
    re_path(r"^(?P<registry_code>\w+)/patient/(?P<patient_id>\d+)/edit$", PatientEditView.as_view(), name='patient_edit'),
    re_path(r'^patientslisting/?', CovidPatientListingView.as_view(), name="patientslisting"),
    re_path(r'^api/v1/', include(('covid.services.rest.urls.api_urls', 'api_urls'), namespace='v1')),
    re_path(r'', include(rdrf_urls)),
]
