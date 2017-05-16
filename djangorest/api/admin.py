from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import BucketList


class BucketListAdmin(ModelAdmin):
    list_display = ('name', 'owner', 'date_created', 'date_modified')
    list_filter = ('owner',)
    search_fields = ('name',)


admin.site.register(BucketList, BucketListAdmin)
