from django.contrib import admin
from .models import Company


class CompanyAdminView(admin.ModelAdmin):
    list_display = ['brand', 'account_number', 'created_at', 'updated_at']
    list_display_links = ['brand', ]
    list_max_show_all = 25


# Register a view for models

admin.site.register(Company, CompanyAdminView)
