from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import generics

from client_panel.models.header import *
from client_panel.serializers.headerSR import *
from client_panel.models.about import *
from client_panel.serializers.aboutSR import *


class ContactView(APIView):
    def get(self, request):
        logos = Logo.objects.all()  # Logolar ro'yxatini olish
        phones = Phone.objects.all()  # Telefonlar ro'yxatini olish
        socials = Social.objects.all()  # Ijtimoiy tarmoqlar ro'yxatini olish
        addresses = Address.objects.all()  # Manzillar ro'yxatini olish
        # JSON javob qaytarish uchun serializerlarni yaratish
        logo_serializer = LogoSerializer(logos, many=True)
        phone_serializer = PhoneSerializer(phones, many=True)
        social_serializer = SocialSerializer(socials, many=True)
        address_serializer = AddressSerializer(addresses, many=True)

        return Response({  # Response obyekti orqali JSON javob qaytarish
            'logos': logo_serializer.data,
            'phones': phone_serializer.data,
            'socials': social_serializer.data,
            'addresses': address_serializer.data
        })


class AboutView(APIView):
    def get(self, request):
        # Birinchi About obyektini olish
        about = About.objects.first()
        # About obyekti uchun serializer yaratish
        about_serializer = AboutSerializer(about)
        # JSON javob qaytarish
        return Response({
            'about': about_serializer.data
        })


class FullAboutView(AboutView):
    def get(self, request):
        # Barcha Experience obyektlarini olish
        experiences = Experience.objects.all()
        # Barcha Certificate obyektlarini olish
        certificates = Certificate.objects.all()

        # Experience va Certificate uchun serializerlarni yaratish
        experience_serializer = ExperienceSerializer(experiences, many=True)
        certificate_serializer = CertificateSerializer(certificates, many=True, context={
            'request': request})  # request serilaizerda urlni olish uchun .

        # AboutView klasining get metodini chaqirib olish va uning javobini qo'shish
        return Response({
            'about': super().get(request).data,
            'experience': experience_serializer.data,
            'certificate': certificate_serializer.data
        })
