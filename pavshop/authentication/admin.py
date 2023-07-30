from django.contrib import admin
from .models import User




# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('bio', 'image', 'major', 'gender', 'first_name', 'last_name', 'is_active', 'username', 'email')


# class AddressAdmin(admin.ModelAdmin):
#     list_display = ('location', 'country', 'city', 'phone')


# admin.site.register(User, UserAdmin)
# admin.site.register(Address, AddressAdmin)
admin.site.register(User)