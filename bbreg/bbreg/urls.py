from django.conf.urls import patterns, include, url
from django.contrib import admin
from repos import api_01

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbreg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', view=include(api_01.urls)),
)





