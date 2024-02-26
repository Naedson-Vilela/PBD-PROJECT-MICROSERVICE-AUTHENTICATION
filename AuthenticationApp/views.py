from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken, TokenError

from .models import UserData, Service, Group, Permission, UserService, UserGroup
from .serializers import UserSerializer, ServiceSerializer, GroupSerializer, PermissionSerializer, \
    UserServiceSerializer, UserGroupSerializer
from rest_framework.response import Response
from rest_framework import status


from rest_framework.permissions import IsAuthenticated


# view for registering users
class RegisterView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        users = UserData.objects.all()
        userSerializer = UserSerializer(users, many=True)
        return JsonResponse(userSerializer.data, safe=False)


class TokenValidationView(APIView):
    def post(self, request):
        token = request.headers.get('Authorization').split(' ')[1]

        try:
            # Verifica se o token é válido e não expirou
            access_token = AccessToken(token)
            access_token.verify()


            return Response({'message': 'Token válido'}, status=status.HTTP_200_OK)
        except TokenError as e:
            # Captura qualquer erro relacionado ao token
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

class ServiceApiView(generics.ListCreateAPIView):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class GroupApiView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionApiView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class UserServiceApiView(generics.ListCreateAPIView):
    queryset = UserService.objects.all()
    serializer_class = UserServiceSerializer

class UserGroupSerialzierApiView(generics.ListCreateAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer