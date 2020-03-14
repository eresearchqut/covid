from django.conf.urls import include
from django.urls import re_path

from rdrf.urls import urlpatterns as rdrf_urlpatterns

rdrf_urls = [p for p in rdrf_urlpatterns if not getattr(p, 'app_name', None) == 'api_urls']

urlpatterns = [
    # Any custom URLs go here before we include the TRRF urls
    re_path(r'^api/v1/', include(('covid.services.rest.urls.api_urls', 'api_urls'), namespace='v1')),
    re_path(r'', include(rdrf_urls)),
]
