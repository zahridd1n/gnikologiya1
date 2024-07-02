from django.contrib import admin
from client_panel.models.about import *
from client_panel.models.category import *
from client_panel.models.calendar import *
from client_panel.models.about import *
from client_panel.models.header import *
from client_panel.models.user import *


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
    list_display = ['icon', 'link']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'longitude', 'latitude']


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['phone']


class ResultAdmin(admin.ModelAdmin):
    list_display = ['name', 'descriptions']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['descriptions','photo' ]


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions', 'number']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession', 'description']


class EducationAdmin(admin.ModelAdmin):
    list_display = ['text']


class EducationProAdmin(admin.ModelAdmin):
    list_display = ['text']

class ClinicalAdmin(admin.ModelAdmin):
    list_display = ['text',"image"]

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['text']

class CertificateAdmin(admin.ModelAdmin):
    list_display = ['image',]


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'confirm']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

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
admin.site.register(Certificate,CertificateAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(EducationPro,EducationProAdmin)
admin.site.register(AboutClinical,ClinicalAdmin)
admin.site.register(Services,ServiceAdmin)


