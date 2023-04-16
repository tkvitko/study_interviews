from django.contrib import admin
from .models import Good


class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'price', 'unit', 'vendor')


admin.site.register(Good, GoodAdmin)
