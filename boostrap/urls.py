from django.urls import path
from .import views

app_name = 'boostrap'

urlpatterns = [
    path('',views.sadika,name='sadika')
]
