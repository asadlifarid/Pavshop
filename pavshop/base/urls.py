from django.urls import path
# from django.contrib import admin
from base.views import base_page, contact_page, thanks_page, about_us_page, home, ContactView, HomeView, AboutView
from .models import Newsletter  # baxarsan

urlpatterns = [
    
    # path('', home, name='home'),
    path('', HomeView.as_view(), name='home'),

    path('base/', base_page, name='base_page'),
    # path('contact/', contact_page, name='contact_page'),  -> function based view ucun
    path('contact/', ContactView.as_view(), name='contact_page'),
    # path('about_us/', about_us_page, name='about_us_page'),
    path('about_us/', AboutView.as_view(), name='about_us_page'),

    path('contact/thanks-for-contacting-us/', thanks_page, name='thanks_page'),

]
