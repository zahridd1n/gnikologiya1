from rest_framework import serializers
from client_panel.models.about import *


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['name', 'profession', 'description','image' ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['text',]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['text',]

class EducationProSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationPro
        fields = ['text',]

class CertificateSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = ['image',]

    def get_image(self, obj):
        # Obj bo'yicha light maydoni uchun URL olish
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None
class AboutClinicalSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = AboutClinical
        fields = ['text', 'image']

    def get_image(self, obj):
        # Obj bo'yicha light maydoni uchun URL olish
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

