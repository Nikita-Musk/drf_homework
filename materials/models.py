from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    preview = models.ImageField(upload_to="courses/preview", verbose_name="Превью курса", blank=True, null=True)
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание курса"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')
    preview = models.ImageField(upload_to="lessons/preview", verbose_name="Превью урока", blank=True, null=True)
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание урока"
    )
    video_url = models.URLField(verbose_name='Ссылка на видео', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курсы', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"