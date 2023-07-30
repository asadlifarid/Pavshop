from django.urls import path
from base.models import Team, Sponsor, Contact, Newsletter
from base.api.views import (
    teams, 
    sponsors, 
    contacts, 
    TeamCreateAPIView, 
    SponsorCreateAPIView, 
    ContactCreateAPIView, 
    ContactRetrieveUpdateDestroyAPIView,
    SponsorRetrieveUpdateDestroyAPIView,
    TeamRetrieveUpdateDestroyAPIView,
    NewsletterCreateAPIView
    )


urlpatterns = [
    # path('teams/', teams, name='teams'),
    path('teams/', TeamCreateAPIView.as_view(), name='teams'),
    path('teams/<int:pk>/', TeamRetrieveUpdateDestroyAPIView.as_view(), name='teams'),
    # path('sponsors/', sponsors, name='sponsors'),
    path('sponsors/', SponsorCreateAPIView.as_view(), name='sponsors'),
    path('sponsors/<int:pk>/', SponsorRetrieveUpdateDestroyAPIView.as_view(), name='sponsors'),
    # path('contacts/', contacts, name='contacts'),
    path('contacts/', ContactCreateAPIView.as_view(), name='contacts'),
    path('contacts/<int:pk>/', ContactRetrieveUpdateDestroyAPIView.as_view(), name='contacts'),
    path('newsletter/', NewsletterCreateAPIView.as_view(), name='newsletter'),
    


]
