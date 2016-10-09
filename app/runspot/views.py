from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import JsonResponse
import requests


class SearchView(TemplateView):
    template_name = 'runspot/search.html'


class AutoCompleteView(View):
    
    def get(self, request, *args, **kwargs):
        text = request.GET.get('text')
        r = requests.get(
            'https://hacker235:pBo8BAC2Xu@distribution-xml.booking.com/json/bookings.autocomplete?'+\
            'text={}&languagecode=en'.format(text)
        )
        labels = [{'label': x['label'], 'dest_id': x['city_ufi'] or x['dest_id']} for x in r.json()]
        return JsonResponse(labels, safe=False)


class HotelsListView(View):

    def get(self, request, *args, **kwargs):
        city_id = request.GET.get('city_id')
        req = 'https://hacker235:pBo8BAC2Xu@distribution-xml.booking.com/json/bookings.getHotels'
        if city_id:
            req += '?city_ids={}'.format(city_id)
        r = requests.get(req)
        '''hotels = [{
            'name': x['name'],
            'address': x['address'],
            'hotel_id': x['hotel_id'],
            'latitude': x['location']['latitude'],
            'longitude': x['location']['longitude']
        } for x in r.json()]'''
        return JsonResponse({'hotels': r.json()}, safe=False)
        

class HotelView(View):

    def get(self, request, *args, **kwargs):
        hotel_id = kwargs.get('hotel_id')
        req = 'https://hacker235:pBo8BAC2Xu@distribution-xml.booking.com/' + \
              'json/bookings.getHotels?hotel_ids={}'.format(hotel_id)
        hotel = requests.get(req)
        x = hotel.json()[0]
        trail_req = 'https://trailapi-trailapi.p.mashape.com/?' + \
            'lat={}&lon={}&limit=25'.format(
                x['location']['latitude'], x['location']['longitude'])
        trail = requests.get(trail_req, headers={
            'X-Mashape-Key': 'vuB0epoteBmsh0AGmCn7TMUYflKgp1sVcMPjsnA7BlatcCvEaK',
            'Accept': 'text/plain'})
        activities = []
        for t in trail.json()['places']:
            activities.extend(t['activities'])
        context = {
            'name': x['name'],
            'address': x['address'],
            'hotel_id': x['hotel_id'],
            'latitude': x['location']['latitude'],
            'longitude': x['location']['longitude'],
            'url': x['url'],
            'trails': trail.json()['places']
        }
        return JsonResponse(context, safe=False)
        

class CitySearchView(TemplateView):
    template_name = 'runspot/citysearch.html'


class TrailsListView(TemplateView):
    template_name = 'runspot/trailslist.html'
    
    def get_context_data(self, *args, **kwargs):
        city = self.request.GET.get('city').split(',')[0]
        city_id = self.request.GET.get('city_id')
        trail_req = 'https://trailapi-trailapi.p.mashape.com/?' + \
            'q[city_cont]'.format(city)
        trail = requests.get(trail_req, headers={
            'X-Mashape-Key': 'vuB0epoteBmsh0AGmCn7TMUYflKgp1sVcMPjsnA7BlatcCvEaK',
            'Accept': 'text/plain'})
        return {'city': city, 'city_id': city_id, 'trails': trail.json()['places']}
        

class TrailView(TemplateView):
    template_name = 'runspot/trail.html'

    def get_context_data(self, *args, **kwargs):
        lat = self.request.GET.get('lat')
        lon = self.request.GET.get('lon')
        req = 'https://hacker235:pBo8BAC2Xu@distribution-xml.booking.com/json/bookings.getHotels?'+\
            'latitude={}&longitude={}'.format(lat, lon)
        r = requests.get(req)
        print(r.json())
        return {'trail': self.request.GET, 'hotels': r.json()} 
