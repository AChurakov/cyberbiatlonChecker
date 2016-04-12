from django.shortcuts import render
from annoying.decorators import render_to
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .poll_api import Api

# Create your views here.


@csrf_protect
def api(request, method_name):
    poll_api = Api()
    poll_api.method = method_name
    poll_api.team_name = request.POST.get('team_name', None)
    poll_api.flag = request.POST.get('flag', None)


    data = poll_api.select_method()


    return JsonResponse(data)