from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import django.contrib.auth.views as auth_views
# from tournament.views import RegisterFormView
from tournament.views import RegisterFormView

urlpatterns = [
    url(r'^api-token-auth/$', obtain_jwt_token, name='obtain-token'),
    url(r'^login/$', auth_views.login, {'template_name': 'website/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/$', RegisterFormView.as_view(), name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('tournament.urls', namespace='tournament')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns() + \
    static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
