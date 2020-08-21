from django.shortcuts import render
import json
from django.http import JsonResponse , HttpResponse
from django.core.serializers import serialize
from django.views.generic import  TemplateView
from .models import County
# Create your views here.

class MainPageView(TemplateView):
    template_name = 'county/main.html'

def county_view(request):
    counties = serialize('geojson', County.objects.all())
    #return HttpResponse(counties, content_type='application/json')
    return JsonResponse(json.loads(counties))

