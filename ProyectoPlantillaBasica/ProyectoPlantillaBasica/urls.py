from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'app.views.inicio', name='inicio'),
	url(r'^inicio2/$', 'app.views.inicio2', name='inicio2'),
    # Examples:
    # url(r'^$', 'ProyectoPlantillaBasica.views.home', name='home'),
    # url(r'^ProyectoPlantillaBasica/', include('ProyectoPlantillaBasica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
