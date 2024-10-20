from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserViewSet

app_name = UsersConfig.name

route = routers.SimpleRouter()
route.register('', UserViewSet, basename='users')

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),

] + route.urls