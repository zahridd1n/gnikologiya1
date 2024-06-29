
from django.urls import path

from client_panel.views.header import ContactView,AboutView,FullAboutView

urlpatterns = [
  

    path('view_contact/', ContactView.as_view()),
    path('about_doctor/', AboutView.as_view()),
    path('fullabout_doctor/', FullAboutView.as_view()),
    
    




    
]