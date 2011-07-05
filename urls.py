from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(r'^login/$', 'django.contrib.auth.views.login', {
            "template_name": "login.html"}, name='login'),
        url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
        url(r'^register/$', 'csrf.views.register', name='register'),
        url(r'^post/$', 'csrf.views.post', name='post'),
        url(r'^$', 'csrf.views.main', name='main'),
    # Example:
    # (r'^CSRFIssue/', include('CSRFIssue.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
