from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.get_all_products)
]
