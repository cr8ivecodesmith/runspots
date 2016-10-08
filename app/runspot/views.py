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
        print(city_id)
        req = 'https://hacker235:pBo8BAC2Xu@distribution-xml.booking.com/json/bookings.getHotels'
        if city_id:
            req += '?city_ids={}'.format(city_id)
        r = requests.get(req)
        context = {'data': r.json()}

        return context
        
        
