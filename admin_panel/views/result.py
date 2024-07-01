from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from client_panel.models import header
from admin_panel.serializers import headerSR


# from client_panel.models.about import *
# from client_panel.serializers.aboutSR import *


# --------------------------Natija ---------------------


class ResultCreate(generics.CreateAPIView):
    """Admin panelda Natija yaratish apisi"""
    queryset = header.Result.objects.all()
    serializer_class = headerSR.ResultSerializer


class ResultList(generics.ListAPIView):
    """Admin panelda Natijalarni oxirgi 8 tasini  ro'yxatini olish apisi"""
    queryset = header.Result.objects.filter().order_by('-id')[:8]
    serializer_class = headerSR.ResultSerializer


class ResultDelete(generics.DestroyAPIView):
    """Admin panelda Natijani o'chirish apisi"""
    queryset = header.Result.objects.all()
    serializer_class = headerSR.ResultSerializer
    lookup_field = 'id'


class ResultUpdate(generics.RetrieveUpdateAPIView):
    """Admin panelda Natijani o'zgartirish apisi"""
    queryset = header.Result.objects.all()
    serializer_class = headerSR.ResultSerializer
    lookup_field = 'id'

