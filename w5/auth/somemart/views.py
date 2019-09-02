import json

import django
from django.http import HttpResponse, JsonResponse
from django.views import View
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
import base64

from .models import Item, Review

SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://example.com/product.schema.json",
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "maxLength": 64,
            "minLength": 1,
        },
        "description": {
            "type": "string",
            "maxLength": 1024,
        },
        "price": {
            "type": "integer",
            "minimum": 1,
            "maximum": 1000000,
        },
    },
    "required": [ "title", "description", "price" ]
}

SCHEMA_REVIEW = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://example.com/product.schema.json",
    "type": "object",
    "properties": {
        "text": {
            "type": "string",
            "maxLength": 1024,
            "minLength": 1,
        },
        "grade": {
            "type": "integer",
            "minimum": 1,
            "maximum": 10,
        },
    },
    "required": [ "text", "grade" ]
}

@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request):
        # Auth stuff
        try:
            # header should be like: Basic __base64_login:password__
            creds = request.META.get('HTTP_AUTHORIZATION')
            creds = creds.split(' ')[1]
            creds = base64.b64decode(creds).decode("utf-8")
            creds = creds.split(':')
            
            user = authenticate(username=creds[0], password=creds[1])
        except Exception as e:
            return JsonResponse({"message": "Cant decode headers, auth failed: {}".format(e)}, status=401)
        
        if user is None:
            return JsonResponse({}, status=401)
        if user.is_staff:
            
            # adding
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
            
        else:
            return JsonResponse({}, status=403)
            
        

@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        try:
            data = json.loads(request.body)
            validate(data, SCHEMA_REVIEW)
            review = Review(text=data["text"], grade=data["grade"], item=Item.objects.get(pk=item_id))
            review.save()
        except django.core.exceptions.ObjectDoesNotExist:
            return JsonResponse({ "error": "Cant find item" }, status=404)
        except json.decoder.JSONDecodeError:
            return JsonResponse({ "error": "Cant parse JSON" }, status=400)
        except ValidationError:
            return JsonResponse({ "error": "Validation error" }, status=400)
        except Exception as e:
            return JsonResponse({ "error": "Something went wrong", "message": str(e) }, status=400)
            
        return JsonResponse({ "id": review.pk }, status=201)


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        try:
            item = Item.objects.get(pk=item_id)
            reviews = []
            
            reviews_data = Review.objects.filter(item=item).order_by('-pk')[:5]
            
            for r in reviews_data:
                reviews.append({
                    "id": r.pk,
                    "text": r.text,
                    "grade": r.grade
                })
            
            data = {
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "price": item.price,
                "reviews": reviews
            }
            return JsonResponse(data, status=200)
            
        except Item.DoesNotExist:
            return JsonResponse({"message": "Item not found"}, status=404)
        
