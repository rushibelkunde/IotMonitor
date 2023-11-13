# urls.py

from django.urls import path
from .views import CreateDevice, GetDevice, DeviceGraphView, ReadingView, Home

# all api endpoints 
urlpatterns = [
    path('', Home , name= "home"),
    path('api/devices/', CreateDevice, name='CreateDevice'),
    path('api/devices/<str:uid>/', GetDevice, name='GetDevice'),
    path('api/devices/<str:uid>/readings/<str:parameter>/', ReadingView, name='ReadingView'),
    path('devices-graph/<str:uid>/', DeviceGraphView, name='device-graph'),
]
