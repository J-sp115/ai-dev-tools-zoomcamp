from django.test import TestCase
from .models import Task

class TaskModelTests(TestCase):
    def test_create_task(self):
        t = Task.objects.create(title="Test task")
        self.assertEqual(str(t), "Test task")
        self.assertFalse(t.completed)
