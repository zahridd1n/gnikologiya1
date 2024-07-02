from rest_framework import serializers
from client_panel.models.category import Category,SubCategory,Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','content','image1','image2','image3','video_link','sub_category','parent']
        
    def get_image1_url(self, obj):
        # Obj bo'yicha image1 maydoni uchun URL olish
        if obj.image1:
            return self.context['request'].build_absolute_uri(obj.image1.url)
        return None

    def get_image2_url(self, obj):
        # Obj bo'yicha image2 maydoni uchun URL olish
        if obj.image2:
            return self.context['request'].build_absolute_uri(obj.image2.url)
        return None

    def get_image3_url(self, obj):
        # Obj bo'yicha image3 maydoni uchun URL olish
        if obj.image3:
            return self.context['request'].build_absolute_uri(obj.image3.url)
        return None