from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
from django.views.generic.base import TemplateView, RedirectView

from LTL.presenters import views as presenter_views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LTL.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'', include('social_auth.urls')),

    url(r'^complete/twitter/get-started/$', RedirectView.as_view(url=reverse_lazy('social_auth_new_user'))),
    # Users who have just registered land here
    url(r'^get-started/$',
        presenter_views.GetStartedView.as_view(),
        name="social_auth_new_user"),

    # Existing user login
    # url(r'^upcoming/', schedule_views.Upcoming.as_view(), name='schedule_upcoming'),
    url(r'^upcoming/$', TemplateView.as_view(template_name='schedule/upcoming.html'), name='schedule_upcoming'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
