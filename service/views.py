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
    if request.POST['team_name']:
        poll_api.team_name = request.POST['team_name']
    else:
        poll_api.team_name = None
    if request.POST['flag']:
        poll_api.flag = request.POST['flag']
    else:
        poll_api.flag = request.POST['flag']

    data = poll_api.select_method()


    return JsonResponse(data)