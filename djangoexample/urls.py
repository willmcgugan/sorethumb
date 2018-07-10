
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from thumbs.views import examples

def project_path(d):
    path = os.path.split(__file__)[0]
    return os.path.join(path, d)


urlpatterns = [
    # Example:
    # (r'^djangoexample/', include('djangoexample.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),

    url(r'^$', examples),

    url(r'^media/(?P<path>.*)', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),

]
