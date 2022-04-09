from django.urls import path
from e_learning.api.api import padre_api_view

urlpatterns=[
    path("padres/",padre_api_view,name="padres_api")
]