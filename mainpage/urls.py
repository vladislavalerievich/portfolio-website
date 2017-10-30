from django.conf.urls import url
from .views import ProjectListAndFormView

urlpatterns = [
    url(r'^$', ProjectListAndFormView.as_view(), name='main')
]
