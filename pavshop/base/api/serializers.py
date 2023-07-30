from rest_framework import serializers
from base.models import Team, Sponsor, Contact, Newsletter


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'id',
            'full_name',
            'major',
            'image'
        )



class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = (
            'id',
            'image'
        )



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'full_name',
            'email',
            'subject',
            'phone',
            'message'
        )



class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = (
            'email',
            'is_active'
        )
