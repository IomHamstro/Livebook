from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Livebook.views',
    # Examples:
    url(r'^$', 'index', name='index'),
	# url(r'^proc/$', 'process', name='process'),
    url(r'^signin/$', 'sign_in', name='sign_in'),
    url(r'^account/$', 'account', name='account'),
    url(r'^news/$', 'news', name='news'),
    url(r'^rating/$', 'rating', name='rating'),
    url(r'^reviews/$', 'reviews', name='reviews'),
    url(r'^forum/$', 'forum', name='forum'),

    # url(r'^analytics/', include('analytics.urls', namespace='analytics')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
