from django.urls import path
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateViewSet,
                             LessonDestroyViewSet, LessonListViewSet,
                             LessonRetrieveViewSet, LessonUpdateViewSet, SubscriptionAPIView)

app_name = MaterialsConfig.name

route = routers.SimpleRouter()
route.register("", CourseViewSet, basename="courses")

urlpatterns = [
    path("lessons/", LessonListViewSet.as_view(), name="lesson-list"),
    path("lessons/<int:pk>/", LessonRetrieveViewSet.as_view(), name="lesson-retrieve"),
    path("lessons/create/", LessonCreateViewSet.as_view(), name="lesson-create"),
    path(
        "lessons/update/<int:pk>/", LessonUpdateViewSet.as_view(), name="lesson-update"
    ),
    path(
        "lessons/delete/<int:pk>/", LessonDestroyViewSet.as_view(), name="lesson-delete"
    ),
    path("subscribe/", SubscriptionAPIView.as_view(), name="subscribe"),
] + route.urls
