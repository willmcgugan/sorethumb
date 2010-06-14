from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

def project_path(d):
    path = os.path.split(__file__)[0]    
    return os.path.join(path, d)

#def testserve(request, path, document_root):
    
#    print "****"    
#    print path
#    print document_root
    
    
urlpatterns = patterns('',
    # Example:
    # (r'^djangoexample/', include('djangoexample.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'thumbs.views.examples'),
    
    url(r'^media/(?P<path>.*)', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),

)
