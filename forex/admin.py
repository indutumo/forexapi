from django.contrib import admin
from .models import *

class ForexRateAdmin(admin.ModelAdmin):
    list_display = ('target_currency','base_currency','rate','datetime')
    list_filter = ['target_currency']
    search_fields = ['target_currency']

admin.site.register(ForexRate, ForexRateAdmin)
