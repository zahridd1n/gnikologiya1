from django.urls import path

from client_panel.views.header import ContactView, AboutView,HeaderView 
from client_panel.views.auth import register, log_out, log_in
from client_panel.views.articles import ArticleListAPIView,NavbarView
from client_panel.views.booking import CreateBooking
from client_panel.views.calculator import PregnancyDetailView

urlpatterns = [

    path('view_contact/', ContactView.as_view(),name="Contact Malumotlari"),
    path('about_doctor/<str:str>', AboutView.as_view()),
    # path('fullabout_doctor/', FullAboutView.as_view()),
    path('articles.view/<int:id>',     ArticleListAPIView.as_view()),
    path('navbar/', NavbarView.as_view()),
    path('booking_post/', CreateBooking.as_view()),
    path('homepage/', HeaderView.as_view()),
    path('calculator/', PregnancyDetailView.as_view(), name='calculator'),




    # ---------------authanticate -----------------------
    path('register/', register),
    path('login/', log_in),
    path('logout/', log_out),

]
