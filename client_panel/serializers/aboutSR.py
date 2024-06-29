from rest_framework import serializers
from client_panel.models.about import *

class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ['name', 'profession', 'description', 'title', 'description1']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields=['text']

class CertificateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='image', label="Rasm")

    class Meta:
        model = Certificate
        fields = ['image']