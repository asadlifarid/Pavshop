from django.contrib import admin
from .models import *
from .forms import NewsletterForm, ContactForm
# from base.models import Contact


class NewsletterAdmin(admin.ModelAdmin):
    # form = NewsletterForm
    list_display = ('email', 'is_active', 'created_at')


class ContactAdmin(admin.ModelAdmin):
    # form = ContactForm
    list_display = ('full_name', 'email', 'phone', 'subject', 'message', 'created_at')



class TeamAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'image', 'major', 'image_tag')
    list_display_links = ('full_name', 'image_tag')
    list_editable = ('major', )


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('image', 'image_tag')





# Register your models here.
admin.site.register(Newsletter, NewsletterAdmin)
# admin.site.register(MailMessage)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(BlockedIps)

