from django.conf.urls import url
from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns

from public import views

urlpatterns = [
    path('',views.IndexView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)