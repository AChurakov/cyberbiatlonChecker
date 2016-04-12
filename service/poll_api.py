import json
from .models import *


class Api():
    def __init__(self):
        self.method = None
        self.team_name = None
        self.flag = None


    def select_method(self):
        methods = {
            'scope': self.scope
        }

        response = methods.get(self.method)()

        return response

    def scope(self):
        teams = Team.objects.all()
        response = {}
        i = 0
        mas = []
        for team in teams:
            i += 1
            mas.append({'team_name': team.team_name,
                        'att_points': team.att_points,
                        'def_points': team.def_points})
        response['response'] = mas
        return response

