import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Cat, Ad


def hello(request):
    return HttpResponse('{"status": "OK"}', status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        add = Ad.objects.all()
        response = []
        for ad in add:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price
            })
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        ad_data = json.loads(request.body)
        ad = Ad.objects.create(
            name=ad_data["name"],
            author=ad_data["author"],
            price=ad_data["price"],
            description=ad_data["description"],
            address=ad_data["address"],
            is_published=ad_data["is_published"]
        )
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        }, safe=False, json_dumps_params={'ensure_ascii': False})


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        }, safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request):
        categories = Cat.objects.all()
        response = []
        for cat in categories:
            response.append({
                "id": cat.id,
                "name": cat.name
            })
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        cat_data = json.loads(request.body)
        cat = Cat.objects.create(
            name=cat_data["name"]
        )
        return JsonResponse({
            "id": cat.id,
            "name": cat.name
        }, safe=False, json_dumps_params={'ensure_ascii': False})


class CatDetailView(DetailView):
    model = Cat

    def get(self, request, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        },
            safe=False, json_dumps_params={'ensure_ascii': False}
        )
