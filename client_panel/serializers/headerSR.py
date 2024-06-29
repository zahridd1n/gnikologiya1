from rest_framework import serializers
from client_panel.models.header import Banner, Logo, Social, Address, Phone, Result, Comment, News

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = 'image'

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['light','dark']

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['name','link',]

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street','longitude','latitude','link']

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['phone']

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
