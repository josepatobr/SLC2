from django.test import TestCase
from .models import UserSingUp
from django.core.exceptions import ValidationError


class Sistema_login_cadastro(TestCase):
    def test_singup_password(self):
        with self.assertRaises(ValidationError):
            UserSingUp.objects.create(name="jose", email="jose@email.com", password="123")

    def test_singup_email(self):
        with self.assertRaises(ValidationError):
            UserSingUp.objects.create(name="jose", email="joseemail.com", password="123456")

    def test_email_duplicado(self):
        UserSingUp.objects.create(name="jose", email="jose@email.com", password="123456")

        with self.assertRaises(ValidationError):
            UserSingUp.objects.create(name="jose1", email="jose@email.com", password="123456")
            
    def test_login_sucesso(self):
        user = UserSingUp.objects.create(name="jose", email="jose@email.com", password="123456")

        response = self.client.post('http://localhost:8000/cassino/login/', {
            'email': 'jose@email.com',
            'password': '123456'
        })

        self.assertEqual(response.status_code, 200)

    def test_login_erro(self):
        user = UserSingUp.objects.create(name="jose", email="jose@email.com", password="123456")
    
        response = self.client.post('http://localhost:8000/cassino/login/', {
            'email': 'jose@email.com',
            'password': '123456'
        })

        self.assertEqual(response.status_code, 200)