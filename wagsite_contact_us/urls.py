from django.urls import path, include

from wagsite_contact_us.views import *

urlpatterns = [
    path('save_contact/', save_contact, name='save_contact'),
]