from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
import base64
from .models import Item, Review

@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request):
        try:
            creds = request.META.get('HTTP_AUTHORIZATION')
            creds = base64.b64decode(creds).decode("utf-8")
            creds = creds.split(':')
            
            user = authenticate(username=creds[0], password=creds[1])
        except Exception as e:
            return JsonResponse({"message": "Cant decode headers, auth failed: {}".format(e)}, status=401)
        
        if user is None:
            return JsonResponse({}, status=401)
        if user.is_staff:
            return JsonResponse({}, status=201)
        else:
            return JsonResponse({}, status=403)
        


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
	# Здесь должен быть ваш код
        return JsonResponse(data, status=200)
