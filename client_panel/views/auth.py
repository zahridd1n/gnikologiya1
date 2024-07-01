from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, permissions

from django.contrib.auth import authenticate
from client_panel.models import User
from rest_framework.parsers import FormParser, MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# -----------------------------register -----------------------------

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'login': openapi.Schema(type=openapi.TYPE_STRING, description='Login username'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
        'password_confirmation': openapi.Schema(type=openapi.TYPE_STRING, description='Password confirmation'),
        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
        'file': openapi.Schema(type=openapi.TYPE_FILE, description='File upload')
    }
), parser_classes=[MultiPartParser, FormParser])  # swagger uchun
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    """ ro'yxatdan o'tish"""
    username = request.data.get('login')
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')
    phone_number = request.data.get('phone_number')
    file = request.data.get('file')

    if not all([username, password, password_confirmation, phone_number, file]):
        return Response({'error': 'Malumotlar to‘liq emas'},
                        status=status.HTTP_400_BAD_REQUEST)  # Forma to'liq to'ldirilmasa

    if password != password_confirmation:
        return Response({'error': 'Password va confirm password bir xil emas'},
                        status=status.HTTP_400_BAD_REQUEST)  # tasdiqlash paroli mos kelmasa

    try:
        user = User.objects.create_user(
            username=username,
            password=password,
            phone_number=phone_number,
            file=file
        )
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)  # token yaratildi
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # token yaratilmadi


# ------------------Login--------------------------------
@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'login': openapi.Schema(type=openapi.TYPE_STRING, description='Login username'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password')
    }
), responses={
    200: openapi.Response(description='Successful login', schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication token')
        }
    )),
    400: 'Bad Request',
    401: 'Unauthorized'
})
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def log_in(request):
    """login qabul  qilingan foydalanuvchilar kirishi uchun """
    username = request.data.get('login')
    password = request.data.get('password')

    if not all([username, password]):
        return Response({'error': 'Username va parol kiritish majburiy'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({'error': 'Login yoki parol noto‘g‘ri'}, status=status.HTTP_401_UNAUTHORIZED)

    if not user.confirm:
        return Response({'error': 'Foydalanuvchi faol emas'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)


# -----------------------------logout------------------------
@swagger_auto_schema(method='post', responses={
    200: openapi.Response(description='Successful logout', schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Logout message')
        }
    )),
    500: 'Internal Server Error'
})
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def log_out(request):
    try:
        token = request.auth
        token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
