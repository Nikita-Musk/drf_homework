from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonCreateViewSet(CreateAPIView):
    serializer_class = LessonSerializer

class LessonUpdateViewSet(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDestroyViewSet(DestroyAPIView):
    queryset = Lesson.objects.all()

class LessonListViewSet(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonRetrieveViewSet(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer