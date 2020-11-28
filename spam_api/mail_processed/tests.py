from django.test import TestCase
from django.contrib.auth.models import User
from .models import Email


# Create your tests here.
class EmailTestCase(TestCase):
    # creamos el entorno de prueba creando usuarios y un thread
    def setUp(self):
        self.user1 = User.objects.create_user('user1',None,'test1234')
        self.user2 = User.objects.create_user('user2',None,'test1234')

        self.email = Thread.Email.create()