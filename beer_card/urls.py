from . import views
from django.urls import path


urlpatterns = [
path('', views.BeerList.as_view(), name='home'),
path('<slug:slug>/', views.beer_detail, name='beer_detail'),
]
