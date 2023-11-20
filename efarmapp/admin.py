from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_farmer', 'is_shop', 'verified')
    list_filter = ('is_shop', 'is_farmer', 'verified')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'name', 'mobile_number', 'profile_picture', 'location', 'address', 'district','verified', 'fruits', 'vegetables')}),
        (_('Bank Info'), {'fields': ('bank_name', 'bank_account_number', 'ifsc_code', 'upi_id')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    list_per_page = 50  # Set the number of users to display per page

admin.site.register(User, CustomUserAdmin)
admin.site.register(Pricechart)
admin.site.register(Productchart)
admin.site.register(Business)
admin.site.register(Doctor)