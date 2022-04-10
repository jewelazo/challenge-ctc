from django.urls import path
from e_learning.api.api import padre_api_view,padre_detail_api_view,EstudianteAPIView,EstudianteDetailAPIView

urlpatterns=[
    path("padres/",padre_api_view,name="padres_api"),
    path("padres/<int:pk>/",padre_detail_api_view,name="padre_detail_api_view"),
    path("estudiantes/",EstudianteAPIView.as_view(),name="estudiantes_api"),
    path("estudiantes/<int:pk>/",EstudianteDetailAPIView.as_view(),name="estudiante_detail_api_view"),
]