import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Item, Review


class AddItemView(View):
    """View для создания товара."""

    def post(self, request):
        # Здесь должен быть ваш код
        return JsonResponse(data, status=201)


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
                "description": "Очень вкусный сыр, да еще и российский.",
                "price": 100,
                "reviews": [{ 
                    "id": 95,
                    "text": "Best. Cheese. Ever.",
                    "grade": 9
                }] 
            }
            return JsonResponse(data, status=200)
            
        except Item.DoesNotExist:
            return JsonResponse({"message": "Item not found"}, status=404)
        
