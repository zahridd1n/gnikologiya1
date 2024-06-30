from django.urls import path

from client_panel.views.header import ContactView, AboutView, FullAboutView
from client_panel.views.auth import register, log_out, log_in

urlpatterns = [

    path('view_contact/', ContactView.as_view()),
    path('about_doctor/', AboutView.as_view()),
    path('fullabout_doctor/', FullAboutView.as_view()),
    # ---------------authanticate -----------------------
    path('register/', register),
    path('login/', log_in),
    path('logout/', log_out),

]
