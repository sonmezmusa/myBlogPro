from django.conf.urls import url, include
from django.contrib import admin
from home.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    url(r'^$', home_view, name='home'),

    url(r'^aboutme/', aboutme_view, name='aboutme'),

    url(r'^contactme/', contactme_view, name='contactme'),

    url(r'^post/', include('post.urls')),

    url(r'^accounts/', include('accounts.urls')),

    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)