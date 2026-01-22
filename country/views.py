from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from json import loads

from country.models import Country


@method_decorator(csrf_exempt, name="dispatch")
class CountryCreateListView(View):

    def post(self, request, *args, **kwargs):

        data = loads(request.body)

        Country.objects.create(**data)

        return JsonResponse({"data" : data, "status" : "201 created"})
    

    def get(self, request, *args, **kwargs):

        qs = Country.objects.all()

        if "region" in request.GET:
            search_region = request.GET.get("region")
            qs = qs.filter(region=search_region)

        if "population_lt" in request.GET:
            search_population = int(request.GET.get("population_lt"))
            qs = qs.filter(population__lt=search_population)

        elif "population_gt" in request.GET:
            search_population = int(request.GET.get("population_gt"))
            qs = qs.filter(population__gt=search_population)


        if "is_independent" in request.GET:
            search_independent = request.GET.get("is_independent")
            qs = qs.filter(is_independent=search_independent)

        data = list(qs.values())

        return JsonResponse({"data" : data, "status" : "200 ok"})
    


@method_decorator(csrf_exempt, name="dispatch")
class CountryRetrieveUpdateDeleteView(View):

    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        data = list(Country.objects.filter(id=id).values())

        return JsonResponse({"data" : data, "status" : "200ok"})
    

    def put(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        data = loads(request.body)

        Country.objects.filter(id=id).update(**data)

        updated_data = list(Country.objects.filter(id=id).values())

        return JsonResponse({"updated_data" : updated_data, "status" : "200 ok"})
    

    def delete(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = Country.objects.get(id=id)

        name = qs.name

        qs.delete()

        return JsonResponse({"message" : f"{name} deleted", "status" : "200 ok"})


    
