from django.urls import path
from . import views

urlpatterns = [
    path('',views.ecom,name='ecom'),
    path('signin/',views.signin,name='signin'),
    path('card/',views.card,name='card'),
]