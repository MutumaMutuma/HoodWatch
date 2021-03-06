from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
# Create your tests here.



class UserTest(TestCase):
    def setUp(self):
        self.user=User(username='lewis',first_name='Lewis',last_name='Mutuma',email='lewismutuma@gmail.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
    
    def test_data(self):
        self.assertTrue(self.user.username,"lewis")
        self.assertTrue(self.user.first_name,"Lewis")
        self.assertTrue(self.user.last_name,'Mutuma')
        self.assertTrue(self.user.email,'lewismutuma@gmail.com')
    
    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)
    
    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)==0)
