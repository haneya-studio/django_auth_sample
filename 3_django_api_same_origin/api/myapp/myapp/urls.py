from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from account.views import UserViewSet, LoginViewSet, LogoutViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'login', LoginViewSet, basename='login')
router.register(r'logout', LogoutViewSet, basename='logout')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]




