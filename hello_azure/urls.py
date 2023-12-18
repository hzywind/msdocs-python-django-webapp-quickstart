from django.urls import path
from . import views
from .views import HelloView

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('api/hello', HelloView.as_view(), name='hello2'),
]