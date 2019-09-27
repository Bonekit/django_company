from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdminView(admin.ModelAdmin):
    list_display = ['brand', 'account_number', 'created_at', 'updated_at']
    list_display_links = ['brand', ]
    list_max_show_all = 25
