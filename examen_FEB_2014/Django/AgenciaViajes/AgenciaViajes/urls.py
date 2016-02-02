from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from viajes import views
from viajes.views import verDestino

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # url(r'^AgenciaViajes/', include('AgenciaViajes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^viajes/', include ('viajes.urls', namespace = 'viajes')),

    url (r'^login', views.userLogin, name='Login'),
    url (r'^logout', views.userLogout, name='Logout'),
)
