from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(
        max_length=35, verbose_name="Телефон", null=True, blank=True
    )
    town = models.CharField(max_length=50, verbose_name="Город", null=True, blank=True)
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    PAYMENT_CHOICES = [("cash", "Наличные"), ("transfer", "Перевод на карту")]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    payment_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата оплаты", null=True, blank=True
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный курс",
        null=True,
        blank=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный урок",
        null=True,
        blank=True,
    )
    amount = models.DecimalField(
        max_digits=15, decimal_places=2, verbose_name="Сумма оплаты"
    )
    payment_method = models.CharField(
        max_length=15, choices=PAYMENT_CHOICES, verbose_name="Способ оплаты"
    )
    session_id = models.CharField(
        max_length=400, verbose_name="ID сессии", blank=True, null=True
    )
    link = models.URLField(
        max_length=400, verbose_name="ссылка на оплату", blank=True, null=True
    )

    def __str__(self):
        return f"Оплата {self.amount} от {self.user}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
