from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from client_panel.models import booking
from client_panel.models import user
from admin_panel.serializers import homeSR


# --------------------------Asosiy sahifa ---------------------

@api_view(['GET'])
def home(request):
    """Admin paneldagi Asosiy sahifa"""
    booking_count = booking.Booking.objects.filter().count()  # qabulga yozilganlar soni
    user_count = user.User.objects.filter(is_staff=False).count()  # ro'yxatdan o'tkanlar soni

    data = {
        'booking_count': booking_count,
        'user_count': user_count,
    }

    return Response(
        {
            'success': True,  # Operatsiyaning muvaffaqiyatli ekanligini bildiradi
            'message': "Success",  # Muvaffaqiyatli xabar
            "data": data  # Malumotlar
        }
    )
