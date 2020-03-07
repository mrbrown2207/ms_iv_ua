from django.conf.urls import url
from .views import issue, upvote, updissstatus


urlpatterns = [
    url(r'^$', issue, name="issue"),
    url(r'^upvote/(?P<id>\d+)', upvote, name="upvote"),
    url(r'^updissstatus/(?P<id>\d+)', updissstatus, name="updissstatus"),
]
