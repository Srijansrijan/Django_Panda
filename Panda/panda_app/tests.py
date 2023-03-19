from django.test import TestCase
from .models import *


# Create your tests here.

# test for object name is correct or not
class First_TestCase(TestCase):
    """
    def setUp(self):
        pass
    def test_check(self):
        self.assertEqual(1,1)
    """

    def test_objectname(self):
        name = Mymodel.objects.create(name='smash', email='sma@jkas', panda_choice="red")
        self.assertEqual(str(name), 'smarsh')


# test for adding and removing objects from the many to many relationship
class manytomany_testcase(TestCase):
    def setUp(self):
        self.John = Author.objects.create(name='John')
        self.Ramesh = Author.objects.create(name='Ramesh')
        self.Spiderman = Book.objects.create(title='Spiderman')

    def test_addmanytomany(self):
        self.Spiderman.authors.add(self.John, self.Ramesh)
        self.assertEqual(self.Spiderman.authors.count(), 2)
        self.assertIn(self.Ramesh, self.Spiderman.authors.all(), msg="Ramesh hasn't been added")
        self.assertIn(self.John, self.Spiderman.authors.all(), msg="John hasn't been added")

    def test_removemanytomany(self):
        self.Spiderman.authors.add(self.John, self.Ramesh)
        self.Spiderman.authors.remove(self.Ramesh)
        self.assertEqual(self.Spiderman.authors.count(), 1)
        self.assertIn(self.John, self.Spiderman.authors.all(), msg="John has Vanished.")
        self.assertNotIn(self.Ramesh, self.Spiderman.authors.all(), msg="Impossible!!!")

# test for add and remove for one-to-many relationship
class onetomany_testcase(TestCase):
    def setUp(self):
        self.John = Author.objects.create(name='John')
        self.Ramesh = Author.objects.create(name='Ramesh')
        self.Spiderman = Book.objects.create(title='Spiderman')
        self.Spiderman.authors.add(self.John)
        self.Batman = Book.objects.create(title='Batman')
        self.Batman.authors.add(self.Ramesh)

    def test_filterbyauthor(self):
        booK_by_John = Book.objects.filter(authors = self.John)
        self.assertEqual(booK_by_John.count(), 1)
        self.assertIn(self.John, booK_by_John.first().authors.all())
