# -*- coding: utf-8 -*-
import re
import datetime
from django.db import models
from django.db.models import F
from model_utils.managers import PassThroughManager
from ckeditor.fields import RichTextField


#site_re = re.compile('''^([\s\S]*?)\.(.*?)/''') 
#site_re = re.compile('''([\w][\w-]*\.(?:com\.cn|com|cn|net|co|org|gov|cc|biz|info))/''')
site_re = re.compile('''([\w][\w-]*\.(?:[.\w]+))/''')

class TopicQuerySet(models.query.QuerySet):
    
    def get_items():
        list = Topic.objects.all().order_by('position')
        return list

class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    image_entity = models.ImageField(u'产品图片', upload_to='image/%Y-%m-%d')
    title = models.CharField(u'主题标题', max_length=200)
    is_publish = models.BooleanField(u'是否发布', default=True)
    create_time = models.DateField(u'创建时间',auto_now_add=True)
    modify_time = models.DateField(u'修改时间',auto_now=True)
    hit_count = models.IntegerField(u'点击次数', default=0)    

    objects = PassThroughManager.for_queryset_class(TopicQuerySet)()

    def preview(self):
        return '<a href="/topic/{0}" target="_blank">预览</a>'.format(self.id)
    preview.allow_tags = True

    def image_display(self):
        return '<a href="/media/{0}"><img src="/media/{0}" style="width:300px"></a>'.format(self.image_entity)
    image_display.allow_tags = True

    def edit(self):
        return '<a href="/w/manage/garden/topic/{0}/">编辑</a>'.format(self.id)
    edit.allow_tags = True

    class Meta:
        #db_table = 'garden_item'#数据库名
        verbose_name = u'主题'
        verbose_name_plural = u'主题场景'

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    image_entity = models.ImageField(u'产品图片', upload_to='image/%Y-%m-%d')
    brand = models.CharField(u'品牌名', max_length=200)
    ratio = models.FloatField(u'图片宽高比', default=0.5)
    title = models.CharField(u'产品名', max_length=200)
    url = models.URLField(u'产品链接', max_length=500)
    original_price = models.FloatField(u'原价', default=0.0, blank=True)
    is_discount = models.BooleanField(u'是否打折')
    sell_price = models.FloatField(u'现价')
    currency = models.CharField(u'货币单位', max_length=10)
    position = models.IntegerField(u'位置')
    
    create_time = models.DateField(u'创建时间', auto_now_add=True)
    modify_time = models.DateField(u'修改时间', auto_now=True)
    hit_count = models.IntegerField('点击次数', default=0)

    topic = models.ForeignKey( Topic)  
 
    def image_display(self):
        return '<a href="/media/{0}"><img src="/media/{0}" style="width:50px"></a>'.format(self.image_entity)
    image_display.allow_tags = True

    def edit(self):
        return '<a href="/w/manage/garden/item/{0}/">编辑</a>'.format(self.id)
    edit.allow_tags = True

    def topic_display(self):
        return '<a href="/w/manage/garden/topic/%d/">%s</a>' % (self.topic.id, self.topic.title)
    topic_display.allow_tags = True

    def get_site(self):
        matched = site_re.search(self.url)
        if matched:
            #return matched.group(2)
            return matched.group(1)
        return ''
  
    def get_sell_price(self):
        price = int(self.sell_price)
        if self.sell_price == price:
            return price
        else:
            return self.sell_price

    def get_original_price(self):
        price = int(self.original_price)
        if self.original_price == price:
            return price
        else:
            return self.original_price


    class Meta:
        #db_table = 'garden_item'#数据库名
        verbose_name = u'单品'
        verbose_name_plural = u'单品中心'
