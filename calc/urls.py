from django.urls import path

from .views import *

urlpatterns = [
    path('calc/form', OrderPre.as_view(), name = 'order_pre_url'),
    path('calc', quantity),
    path('', quantity),
]