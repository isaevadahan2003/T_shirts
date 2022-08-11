from django.urls import path
from . import views

app_name = 'T_shirts'

urlpatterns = [
    path('', views.T_shitrsView.as_view(), name='list1')
]