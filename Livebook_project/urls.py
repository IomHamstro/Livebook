from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from Livebook.views import ReviewsView, NewsView

admin.autodiscover()

urlpatterns = patterns('Livebook.views',
    # Examples:
    url(r'^$', 'index', name='index'),
    url(r'^signin/$', 'sign_in', name='sign_in'),
    url(r'^error/$', 'error', name='error'),
    url(r'^account/$', 'account', name='account'),

    url(r'^news/$',  NewsView.as_view(), name='news'),
    url(r'^news(?P<page>\d+)$',  NewsView.as_view(), name='news'),


    url(r'^rating/$', 'rating', name='rating'),

    url(r'^reviews/$', ReviewsView.as_view(), name='reviews'),
    url(r'^reviews(?P<page>\d+)$', ReviewsView.as_view(), name='reviews'),

    url(r'^forum/$', 'forum', name='forum'),
    url(r'^registration', 'registration', name='registration'),
    url(r'^book(?P<id>\d+)$', 'book', name='book'),
    url(r'^book_list$', 'book_list', name='book_list'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
