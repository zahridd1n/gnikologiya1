from rest_framework import serializers
from client_panel.models.header import Banner, Logo, Social, Address, Phone, Result, Comment, News,Services


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = 'image'

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['light','dark']

    def get_light(self, obj):
        if obj.light:
            return self.context['request'].build_absolute_uri(obj.light.url)
        return None

    def get_dark(self, obj):
        if obj.dark:
            return self.context['request'].build_absolute_uri(obj.dark.url)
        return None


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['icon','link',]

        def get_icon(self, obj):
            if obj.icon:
                return self.context['request'].build_absolute_uri(obj.icon.url)
            return None

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street','longitude','latitude']

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


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
