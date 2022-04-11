from django.urls import reverse,resolve
from django.test import SimpleTestCase
from e_learning.api.api import PadreAPIView
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.

class ApiUrlsTest(SimpleTestCase):

    def test_get_padres_is_resolved(self):
        url=reverse("padres_api")
        self.assertEqual(resolve(url).func.view_class,PadreAPIView)


class ApiPadresTest(APITestCase):

    def test_create_padre_with_correct_data(self):
        sample_padre={
            "nombre": "Test",
            "apellidos": "Testing",
            "nacionalidad": "Ucrania",
            "genero": "M",
            "edad": 50,
            "email": "test@mail.com",
            "telefono": "444321786"
        }
        response= self.client.post(reverse("padres_api"),sample_padre)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_no_create_padre_with_incorrect_data(self):
        sample_padre={
            "nombre": "Test",
            "apellidos": "Testing",
            "nacionalidad": "Ucrania",
            "genero": "M",
            "edad": 101,
            "email": "test@mail.com",
            "telefono": "444321786"
        }
        response= self.client.post(reverse("padres_api"),sample_padre)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        