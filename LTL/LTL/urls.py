from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LTL.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'', include('social_auth.urls')),

    url(r'^new-users-redirect-url/',
        TemplateView.as_view(template_name="welcome.html"),
        name="social_auth_new_user"),

    url(r'^admin/', include(admin.site.urls)),
)
