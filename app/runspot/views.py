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
        print(r.json())
        labels = [{'label': x['label'], 'dest_id': x['city_ufi'] or x['dest_id']} for x in r.json()]
        return JsonResponse(labels, safe=False)


class HotelsListView(TemplateView):
    template_name = 'runspot/hotelslist.html'

    def get_context_data(self, *args, **kwargs):
        city_id = self.request.GET.get('city_id')
        req = 'https://hacker235:pBo8BAC2Xu@distribution-xml.booking.com/json/bookings.getHotels'
        if city_id:
            req += '?city_ids={}'.format(city_id)
        r = requests.get(req)
        hotels = [{
            'name': x['name'],
            'address': x['address'],
            'hotel_id': x['hotel_id'],
            'latitude': x['location']['latitude'],
            'longitude': x['location']['longitude']
        } for x in r.json()]
        context = {'hotels': r.json()}
        return context
        

class HotelView(TemplateView):
    template_name = 'runspot/hotel.html'

    def get_context_data(self, *args, **kwargs):
        hotel_id = kwargs.get('hotel_id')
        print(kwargs)
        req = 'https://hacker235:pBo8BAC2Xu@distribution-xml.booking.com/' + \
            'json/bookings.getHotels?hotel_ids={}'.format(hotel_id)
        r = requests.get(req)
        x = r.json()[0]
        print(x)
        context = {
            'name': x['name'],
            'address': x['address'],
            'hotel_id': x['hotel_id'],
            'latitude': x['location']['latitude'],
            'longitude': x['location']['longitude']
        }
        return context
        
