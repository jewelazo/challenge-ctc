from django.urls import path
from e_learning.api.api import PadreAPIView,PadreDetailAPIView,EstudianteAPIView,EstudianteDetailAPIView

urlpatterns=[
    path("padres/",PadreAPIView.as_view(),name="padres_api"),
    path("padres/<int:pk>/",PadreDetailAPIView.as_view(),name="padre_detail_api_view"),
    path("estudiantes/",EstudianteAPIView.as_view(),name="estudiantes_api"),
    path("estudiantes/<int:pk>/",EstudianteDetailAPIView.as_view(),name="estudiante_detail_api_view"),
]