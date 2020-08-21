from django.urls import path
from .views import MainPageView,county_view


urlpatterns = [
    path('countydata/',county_view,name='county'),
    path('',MainPageView.as_view(),name='main'),
]