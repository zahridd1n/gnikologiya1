from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from client_panel.models import header
from admin_panel.serializers import headerSR

# --------------------------Sharh ---------------------


class CommentCreate(generics.CreateAPIView):
    """Admin panelda Sharh yaratish apisi"""
    queryset = header.Comment.objects.all()
    serializer_class = headerSR.CommentSerializer


class CommentList(generics.ListAPIView):
    """Admin panelda Sharhlarni ro'yxatini olish apisi"""
    queryset = header.Comment.objects.filter().order_by('-id')
    serializer_class = headerSR.CommentSerializer


class CommentDelete(generics.DestroyAPIView):
    """Admin panelda Sharhni o'chirish apisi"""
    queryset = header.Comment.objects.all()
    serializer_class = headerSR.CommentSerializer
    lookup_field = 'id'


class CommentUpdate(generics.RetrieveUpdateAPIView):
    """Admin panelda SHarhni o'zgartirish apisi"""
    queryset = header.Comment.objects.all()
    serializer_class = headerSR.CommentSerializer
    lookup_field = 'id'

