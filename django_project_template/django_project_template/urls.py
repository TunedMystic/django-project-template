from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'main.views.login_user', name='login'),
    url(r'^login$', 'main.views.login_user', name='login'),
    url(r'^logout', 'main.views.logout_user', name='logout'),
    # Examples:
    # url(r'^$', 'django_project_template.views.home', name='home'),
    # url(r'^django_project_template/', include('django_project_template.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'main.views.page_not_found'

urlpatterns += patterns('',
    (r'^$', include('app.urls')),
)