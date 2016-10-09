"""can URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.runspot.views import (
    SearchView,
    AutoCompleteView,
    HotelsListView,
    HotelView,
    CitySearchView,
    TrailsListView,
    TrailView,
    MapView,
    HotelTrailView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^citysearch/', CitySearchView.as_view(), name='citysearch'),
    url(r'^trailslist/', TrailsListView.as_view(), name='trailslist'),
    url(r'^trail/', TrailView.as_view(), name='trail'),
    url(r'^map/', MapView.as_view(), name='map'),


    url(r'^auto/', AutoCompleteView.as_view(), name='autocomplete'),
    url(r'^list/', HotelsListView.as_view(), name='hotelslist'),
    url(r'^hotel/(?P<hotel_id>[0-9]+)', HotelView.as_view(), name='hotel'),
    url(r'^hoteltrail/(?P<hotel_id>[0-9]+)', HotelTrailView.as_view(), name='hoteltrail'),
    url('', SearchView.as_view(), name='search'),
]
