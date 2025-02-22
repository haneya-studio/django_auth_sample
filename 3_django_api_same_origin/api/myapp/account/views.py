from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from rest_framework import serializers, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User

from django.http import JsonResponse
from django.middleware.csrf import get_token


def csrf_token_view(request):
    return JsonResponse({"csrfToken": get_token(request)})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated, )


class LoginViewSet(viewsets.ViewSet):
    @method_decorator(csrf_protect)
    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"})
        else:
            return Response({"error": "Invalid credentials"}, status=400)


class LogoutViewSet(viewsets.ViewSet):
    @method_decorator(csrf_protect)
    def create(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"})
