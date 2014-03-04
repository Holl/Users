from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'userproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url('^signup/', 'user_app.views.signup', name='signup'),

    url('^secret/', 'user_app.views.special_page', name='secret'),

    url('^accounts/login', 'user_app.views.login_page', name='login_page')
)
