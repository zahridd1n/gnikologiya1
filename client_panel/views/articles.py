from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import generics

from client_panel.models.header import *
from client_panel.serializers.articleSR import *
from client_panel.models.category import *

class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get(self, request, id):
        # Berilgan sub_category bilan barcha maqolalarni olish
        articles = Article.objects.filter(sub_category=id)
        # Maqolalarni serializatsiya qilish
        article_serialized = ArticleSerializer(articles, many=True).data

        # Maqolalarni id bo'yicha saqlash uchun lug'at yaratish
        articles_dict = {article['id']: article for article in article_serialized}

        # Har bir maqolaga 'children' kalitini qo'shish, bolalarni joylashtirish uchun
        for article in articles_dict.values():
            article['children'] = []

        # Maqolalarni ota-ona id bo'yicha joylashtirish
        for article in article_serialized:
            parent_id = article['parent']
            if parent_id:
                articles_dict[parent_id]['children'].append(article)

        # Ota-onasi bo'lgan maqolalarni filtrlash (ular joylashtirilgan, shuning uchun faqat yuqori darajadagi maqolalar qoladi)
        nested_articles = [article for article in articles_dict.values() if article['parent'] is None]

        return Response(nested_articles)
    

    
class CategoryView(APIView):
    category_serializer_class = CategorySerializer
    subcategory_serializer_class = SubCategorySerializer

    def get(self, request):
        # Barcha kategoriyalarni olish
        categories = Category.objects.all()
        serialized_categories = self.category_serializer_class(categories, many=True).data

        # Har bir kategoriya uchun subkategoriyalarni qo'shish
        for category_data in serialized_categories:
            category_id = category_data['id']
            # Kategoriya ID si boyicha subkategoriyalarni qidirish
            subcategories = SubCategory.objects.filter(category=category_id)
            # Subkategoriyalarni serializatsiya qilish
            serialized_subcategories = self.subcategory_serializer_class(subcategories, many=True).data
            # Kategoriya ma'lumotlariga subkategoriyalarni qo'shish
            category_data['subcategories'] = serialized_subcategories

        # Natijani javob sifatida qaytarish
        return Response(serialized_categories)
    
    
    
