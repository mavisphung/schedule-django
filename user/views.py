from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime
from user import redis_instance
from user.models import User
import time
# Create your views here.
class DemoRedisView(generics.ListAPIView):
    
    def list(self, request, *args, **kwargs):
        # print('before:', datetime.now())
        # redis_instance.set('today', str(datetime.now()), 10)
        # time.sleep(5)
        # print('current:', datetime.now())
        # print('saved date:', redis_instance.get('today'))
        user1 = User(name = 'DefaultUser')
        user2 = User(name = 'Local2User')
        user1.save()
        user2.save(using = 'auth_db')
        return Response()