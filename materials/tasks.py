from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from materials.models import Course, Subscription
from users.models import User


@shared_task
def send_info_about_course_update(course_pk):
    """ Отправляет сообщение об обновлении курса подписанным пользователям. """
    course = Course.objects.filter(id=course_pk).first()
    users = User.objects.all()
    for user in users:
        subs = Subscription.objects.filter(user=user, course=course).first()
        if subs:
            send_mail(
                subject=f'Обновление курса "{course}"',
                message=f'Курс "{course}", на который вы подписаны, обновлен.',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
            print("Письмо с обновлением отправлено")


@shared_task
def check_last_login():
    """ Проверяет активность пользователя. Блокирует при неактивности более месяца. """
    today = timezone.now()
    month_ago = today - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__gte=month_ago, is_active=True)

    for user in inactive_users:
        user.is_active = False
        user.save()
        print(f"Пользователь {user.username} был заблокирован")
