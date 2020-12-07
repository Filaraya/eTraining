from django.test import TestCase
from blog.models import Instructor

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

class InstructorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Instructor.objects.create(first_name='John', last_name='Smith')

    def test_first_name_label(self):
        instructor = Instructor.objects.get(id=1)
        field_label = instructor._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_email_label(self):
        instructor= Instructor.objects.get(id=1)
        field_label = instructor._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_first_name_max_length(self):
        instructor = Instructor.objects.get(id=1)
        max_length = instructor._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        instructor = Instructor.objects.get(id=1)
        expected_object_name = f'{instructor.last_name}, {instructor.first_name}'
        self.assertEqual(expected_object_name, str(instructor))

    def test_get_absolute_url(self):
        instructor = Instructor.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(instructor.get_absolute_url(), '/blog/instructor/1')