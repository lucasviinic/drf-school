from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CT1', descricao='Curso teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CT2', descricao='Curso teste 2', nivel='A'
        )

    def test_falhador(self):
        self.fail('O teste falhou de proposito, não se preocupe :)')