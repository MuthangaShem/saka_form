from django.test import TestCase
from .models import Category, Event


class CategoryTestClass(TestCase):
    """
    Initializing Category Test Class
    """

    def setUp(self):
        self.new_category = Category(
            category_name='Food', category_description='Everything great and sweet!')

    def test_category_instance_true(self):
        self.assertTrue(isinstance(self.new_category, Category))

    def test_save_category_method_true(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 1)

    def test_delete_category_method_true(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.new_category.delete_category()
        self.assertTrue(len(categories) == 0)

    def test_update_category_method_true(self):
        self.new_category.save_category()
        category = self.new_category.update_category(self.new_category.id, 'Music', 'Great Music')
        category = Category.objects.filter(
            category_name='Music', category_description='Great Music').all()
        category_updated = Category.objects.filter(
            category_name='Food', category_description='Everything great and sweet!').all()
        self.assertTrue(len(category) == 1 and len(category_updated) == 0)

    def tearDown(self):
        Category.objects.all().delete()


class EventTestClass(TestCase):
    """
    Initializing Event Test Class
    """

    def setUp(self):
        self.new_event = Event(event_title='test event', event_image='event-images/image.jpg', event_description='event testing',
                               event_location='somewhere', number_of_tickets=50, event_type='eventful', event_topic='event test topic')

    def test_instance_event_true(self):
        self.assertTrue(isinstance(self.new_event, Event))
