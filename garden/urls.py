from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    (r'^topic/(\d+)$', topic),
    (r'^item/(\d+)$', item),
    (r'^topic_api$', topic_api),
)

urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
