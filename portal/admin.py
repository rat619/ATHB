from django.contrib import admin
from .models import article

admin.site.site_header = "ATHB Admin"
admin.site.site_title = "ATHB Admin"
admin.site.index_title = "Welcome to ATHB's Admin Area"

@admin.register(article)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('type','title', 'content', 'created','modified','price')  

