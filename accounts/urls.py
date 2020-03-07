from django.conf.urls import url, include
from accounts import urls_reset
from .views import register, userprofile, logout, login


urlpatterns = [
    url(r'^register/', register, name='register'),
    url(r'^userprofile/', userprofile, name='userprofile'),
    url(r'^logout/', logout, name='logout'),
    url(r'^login/', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]