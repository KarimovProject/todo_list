from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import TodoItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
class GetUser(View):
    def post(self, requser):
        username = requser.POST['username']
        password = requser.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            return JsonResponse({
                'id':user.id,
                'password':user.password,
                'username':user.username
            })
        return JsonResponse({'None User':False})
class Get_all(View):
    def get(self, request):
        todo_all = TodoItem.objects.all()
        todo_all_json = {'results':[]}
        for i in todo_all:
            todo_all_json['results'].append(i.todo_json())
        return JsonResponse(todo_all_json)