from django.urls import path
from rest_framework import routers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentListAPIView, UserCreateAPIView,
                         UserDeleteAPIView, UserListAPIView, UserUpdateAPIView,
                         UserViewSet, PaymentCreateAPIView)

app_name = UsersConfig.name

route = routers.SimpleRouter()
route.register("", UserViewSet, basename="users")

urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment-list"),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment-create"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("list/", UserListAPIView.as_view(), name="users-list"),
    path("<int:pk>/", UserDeleteAPIView.as_view(), name="user-retrieve"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="user-delete"),
] + route.urls
