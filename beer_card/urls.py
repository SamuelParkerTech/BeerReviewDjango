from django.urls import path
from . import views

urlpatterns = [
    path('', views.BeerList.as_view(), name='home'),
    path('<slug:slug>/', views.beer_detail, name='beer_detail'),
    path(
        '<slug:slug>/edit_review/<int:review_id>',
        views.review_edit,
        name='review_edit'
    ),
    path(
        '<slug:slug>/delete_review/<int:review_id>',
        views.review_delete,
        name='review_delete'
    ),
]
