import re

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from localshop.apps.packages.xmlrpc import handle_request

admin.autodiscover()

static_prefix = re.escape(settings.STATIC_URL.lstrip('/'))


urlpatterns = [
    url(r'^$', 'localshop.views.index', name='index'),
    url(r'^dashboard/',
        include('localshop.apps.dashboard.urls', namespace='dashboard')),

    # Default path for xmlrpc calls
    url(r'^RPC2$', handle_request),
    url(r'^pypi$', handle_request),

    url(r'^repo/',
        include('localshop.apps.packages.urls', namespace='packages')),

    url(r'^accounts/', include('localshop.apps.accounts.auth_urls')),
    url(r'^accounts/',
        include('localshop.apps.accounts.urls', namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^%s(?P<path>.*)$' % static_prefix,
        'django.contrib.staticfiles.views.serve', {'insecure': True}),
]
