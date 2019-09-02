import json

from django.http import HttpResponse, JsonResponse
from django.views import View
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Item, Review

SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://example.com/product.schema.json",
    "type": "object",
    "properties": {
        "price": {
            "type": "integer"
        }
    },
    "required": [ "price" ]
}

@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request):
        try:
            data = json.loads(request.body)
            validate(data, SCHEMA)
            item = Item(title=data["title"], description=data["description"], price=data["price"])
            item.save()
        except json.decoder.JSONDecodeError:
            return JsonResponse({ "error": "Cant parse JSON" }, status=400)
        except ValidationError:
            return JsonResponse({ "error": "Validation error" }, status=400)
        except:
            return JsonResponse({ "error": "Something went wrong" }, status=400)
            
        return JsonResponse({ "id": item.pk }, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        # Здесь должен быть ваш код
        return JsonResponse(data, status=201)


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        try:
            item = Item.objects.get(pk=item_id)
            data = {
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "price": item.price,
                "reviews": [{ 
                    "id": 95,
                    "text": "Best. Cheese. Ever.",
                    "grade": 9
                }] 
            }
            return JsonResponse(data, status=200)
            
        except Item.DoesNotExist:
            return JsonResponse({"message": "Item not found"}, status=404)
        
