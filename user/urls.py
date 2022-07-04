from django.urls import path
from user import views

urlpatterns = [
    path('', views.DemoRedisView.as_view(), name = 'demo-redis'),
]