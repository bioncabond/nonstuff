from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Nonstuff

class NonstuffTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_stuff = Nonstuff.objects.create(name='rake', owner=testuser1,description='Better for collecting leaves than a shovel.')
        test_stuff.save()

    def test_stuffs_model(self): 
        nonstuff = Nonstuff.objects.get(id=1)
        actual_owner = str(nonstuff.owner)
        actual_name = str(nonstuff.name)
        actual_description = str(nonstuff.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'rake')
        self.assertEqual(actual_description,'Better for collecting leaves than a shovel.')