from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@gmail.com")
        self.course = Course.objects.create(name="Проверочный курс")
        self.lesson = Lesson.objects.create(
            name="Тестовый урок 1", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse("materials:lesson-create")
        data = {"name": "Тестовый урок 2"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Тестовый урок 1")

    def test_lesson_update(self):
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {"name": "Измененное название урока"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Измененное название урока")

    def test_lesson_delete(self):
        url = reverse("materials:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lesson-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_url": None,
                    "name": self.lesson.name,
                    "preview": None,
                    "description": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@gmail.com")
        self.course = Course.objects.create(name="Проверочный курс")
        self.lesson = Lesson.objects.create(
            name="Тестовый урок 1", course=self.course, owner=self.user
        )
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        url = reverse("materials:subscribe")
        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "подписка удалена")
