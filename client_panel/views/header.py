from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import generics

from client_panel.models.header import *
from client_panel.serializers.headerSR import *
from client_panel.models.about import *
from client_panel.serializers.aboutSR import *
from client_panel.serializers.titles.titles import TAHSIL,ISH_TAJRIBASI,SERTIFIKAT,MALAKA

class ContactView(APIView):
    def get(self, request):
        logos = Logo.objects.all()  # Logolar ro'yxatini olish
        phones = Phone.objects.all()  # Telefonlar ro'yxatini olish
        socials = Social.objects.all()  # Ijtimoiy tarmoqlar ro'yxatini olish
        addresses = Address.objects.all()  # Manzillar ro'yxatini olish

        # JSON javob qaytarish uchun serializerlarni yaratish
        logo_serializer = LogoSerializer(logos, many=True, context={'request': request})
        phone_serializer = PhoneSerializer(phones, many=True)
        social_serializer = SocialSerializer(socials, many=True, context={'request': request})
        address_serializer = AddressSerializer(addresses, many=True)
        data={'logos': logo_serializer.data,
            'phones': phone_serializer.data,
            'socials': social_serializer.data,
            'addresses': address_serializer.data}

        response_data = {  # Response obyekti orqali JSON javob qaytarish
            'success': True,  # Operatsiyaning muvaffaqiyatli ekanligini bildiradi
            'message': "Success",  # Muvaffaqiyatli xabar
            'data':data
        }

        return Response(response_data)
        


class AboutView(APIView):
    def get(self, request, str=None):
        if str == "full":
            return self.get_full_about(request)
        else:
            return self.get_about(request)

    def get_about(self, request):
        about = About.objects.first()
        about_serializer = AboutSerializer(about, context={'request': request})

        data = {
            'about': about_serializer.data
        }

        response_data = {
            'success': True,
            'message': "Success",
            'data': data
        }
        return Response(response_data)

    def get_full_about(self, request):
        experiences = Experience.objects.all()
        certificates = Certificate.objects.all()
        education = Education.objects.all()
        educationPro = EducationPro.objects.all()

        education_serializer = EducationSerializer(education, many=True)
        educationPro_serializer = EducationSerializer(educationPro, many=True)
        experience_serializer = ExperienceSerializer(experiences, many=True )
        certificate_serializer = CertificateSerializer(certificates, many=True, context={'request': request})

        about = About.objects.first()
        about_serializer = AboutSerializer(about, context={'request': request})

        title1={'title':'bobur'}
        data = {
            'about': about_serializer.data,
            'education': education_serializer.data,
            'educationPro': educationPro_serializer.data,
            'experience': experience_serializer.data,
            'certificate': certificate_serializer.data
        }
      
        response_data = {
            'success': True,
            'message': "Success",
            'data': data
        }
        return Response(response_data)
    

class HeaderView(APIView):
    def get(self, request):
        aboutclinic = AboutClinical.objects.first()
        services = Services.objects.all()
        results = Result.objects.all()
        comment = Comment.objects.all()

        aboutclinic_serializer = AboutClinicalSerializer(aboutclinic, context={'request': request})
        services_serializer = ServiceSerializer(services, many=True, context={'request': request})
        results_serializer = ResultSerializer(results, many=True, context={'request': request})
        comment_serializer = CommentSerializer(comment, many=True, context={'request': request})

        data = {
            'aboutclinic': aboutclinic_serializer.data,
            'services': services_serializer.data,
            'results': results_serializer.data,
            'comment': comment_serializer.data}
        
        response_data = {
            'success': True,
            'message': "Success",
            'data': data
        }
        return Response(response_data)