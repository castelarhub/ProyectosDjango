from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.inicio', name='inicio'),
    url(r'^hola/$', 'app.views.hola', name='hola'),
    url(r'^hola2/$', 'app.views.hola2', name='hola2'),
    url(r'^hola3/(\w+)/$', 'app.views.hola3', name='hola3'),
    url(r'.', 'app.views.otro', name='otro'),
    # url(r'^$', 'ProyectoHolaMundo.views.home', name='home'),
    # url(r'^ProyectoHolaMundo/', include('ProyectoHolaMundo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
