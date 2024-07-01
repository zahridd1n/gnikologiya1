from django.contrib import admin
from .models.about import *
from .models.category import *
from .models.calendar import *
from .models.about import *
from .models.header import *
from .models.user import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


class PodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'sub_category']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'sub_category']


class CalendarAdmin(admin.ModelAdmin):
    list_display = ['week_number', 'week_title']


class WeeksArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', "video_link", "week"]


class BannerAdmin(admin.ModelAdmin):
    list_display = ['image']


class LogoAdmin(admin.ModelAdmin):
    list_display = ['light', 'dark']


class SocialAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'longitude', 'latitude', 'link']


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['phone']


class ResultAdmin(admin.ModelAdmin):
    list_display = ['name', 'descriptions']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['photo', 'descriptions']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions', 'number']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession', 'description', 'title']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['text']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'confirm']


admin.site.register(User, UserAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(PodCategory, PodCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Weeks, CalendarAdmin)
admin.site.register(WeekArticle, WeeksArticleAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Logo, LogoAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Certificate)