from rest_framework import serializers
from client_panel.models.header import Banner, Logo, Social, Address, Phone, Result, Comment, News


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
