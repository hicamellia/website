# -*- coding: utf-8 -*-

from django.contrib import admin
from garden import models


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_display', 'original_price', 'is_discount', 'sell_price', 'currency', 'position', 'hit_count', 'topic_display', 'edit')
    raw_id_fields = ('topic', )
    search_fields = ('id', 'title')
 
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title','image_display',  'create_time', 'hit_count', 'is_publish', 'preview', 'edit')
    search_fields = ('id', 'title')


admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Topic, TopicAdmin)
