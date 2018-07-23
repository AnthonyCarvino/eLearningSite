from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

# Create your tests here.

from .models import Course, Step

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="python regular expressions",
            description="learn to write reg expressions",
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)


class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="python testing",
            description="learn to write tests"
        )
        self.course2 = Course.objects.create(
            title="new course",
            description="a new course"
        )
        self.step = Step.objects.create(
            title="Introduction to doctests",
            description="learn to write tests in docstrings",
            course=self.course
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])