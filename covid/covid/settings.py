# flake8: noqa
import os

from rdrf.settings import *
import covid


FALLBACK_REGISTRY_CODE = "covid"
LOCALE_PATHS = env.getlist("locale_paths", ['/data/translations/locale'])

# Adding this project's app first, so that its templates overrides base templates
INSTALLED_APPS = [
    FALLBACK_REGISTRY_CODE,
] + INSTALLED_APPS

ROOT_URLCONF = '%s.urls' % FALLBACK_REGISTRY_CODE

SEND_ACTIVATION_EMAIL = False

PROJECT_TITLE = env.get("project_title", "COVID Clinical Registry Platform")
# PROJECT_TITLE_LINK = "login_router"

PROJECT_LOGO = env.get("project_logo", "images/covid/project_logo.png")

LOGIN_REDIRECT_URL = '/patientslisting'

# Registration customisation (if any) goes here
# REGISTRATION_CLASS = "covid.custom_registration.CustomRegistration"

VERSION = env.get('app_version', '%s (covid)' % covid.VERSION)

# Currently using registration from base TRRF as-is, but keeping these for future reference
#
# REGISTRATION_FORM = 'mnd.forms.mnd_registration_form.MNDRegistrationForm'
# REGISTRATION_CLASS = 'mnd.registry.groups.registration.mnd_registration.MNDRegistration'
