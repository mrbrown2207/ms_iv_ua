from django.conf.urls import url
from .views import issue, upvote


urlpatterns = [
    url(r'^$', issue, name="issue"),
    url(r'^upvote/(?P<id>\d+)', upvote, name="upvote"),
]
