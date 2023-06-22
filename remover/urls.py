from django.urls import path
from . import views

app_name = 'remover'

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('result/', views.result_image, name='result_image'),
]
