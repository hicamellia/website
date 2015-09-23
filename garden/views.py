# -*- coding: utf-8 -*-
import logging
import re
import string
import traceback
import json
# Create your views here.
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from sites.settings import *
# app specific files

from datetime import date, datetime, time, timedelta

LOG = logging.getLogger('django')


class api(object):
    def __init__(self, need_login=False):
        self.need_login = need_login

    def __call__(self, func):
        def _(request):
            try:
                if self.need_login and not request.user.id:
                    json_obj = {'error': 'auth'}
                else:
                    json_obj = func(request) or {}
                return HttpResponse(json.dumps(json_obj))
            except Exception as e:
                traceback.print_exc()
                return HttpResponse(json.dumps({'error': str(e)}))

        return _

def to_dict(**kwargs):
    temp = {}
    for key in kwargs.keys():
        value = kwargs.get(key)[0]
        if value != '':
            temp[key] = value
    return temp

def topic(request, id):
    result = {}
    topic = Topic.objects.get(id = id)
    topic.hit_count = F('hit_count') + 1
    topic.save()
    topic.items_start = 6
    topic.items_length = 6
    items = topic.item_set.all().order_by('position')[0:6]
    result['topic'] = topic
    result['items'] = items
    return render_to_response("topic.html", result, context_instance=RequestContext(request))


def item(request, id):
    item = Item.objects.get(id = id)
    item.hit_count = F('hit_count') + 1
    item.save()
    return HttpResponseRedirect(item.url) 

def topic_api(request):
    result = {}

    id = request.GET.get('id')
    start = int(request.GET.get('start'))
    length = int(request.GET.get('length'))

    topic = Topic.objects.get(id = id)
    items = topic.item_set.all().order_by('position')
    list = []
    if start >= len(items):
        result['items'] = list
        return HttpResponse(json.dumps(result))
    for item in items[start:start + length]:
        dict = {}
        dict['id'] = item.id
        dict['brand'] = item.brand
        dict['ratio'] = item.ratio
        dict['title'] = item.title
        dict['url'] = '/item/' + str(item.id)
        dict['original_price'] = item.get_original_price()
        dict['sell_price'] = item.get_sell_price()
        dict['site'] = item.get_site()
        dict['is_discount'] = item.is_discount
        dict['currency'] = item.currency
        dict['position'] = item.position
        dict['image_entity'] = '/' + MEDIA_URL + item.image_entity.name
        list.append(dict)

    result['items'] = list
    return HttpResponse(json.dumps(result))
     
