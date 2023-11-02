from django.urls import path
from . import views

urlpatterns =[
    path('', views.place_list, name='place_list'),
    path('visited', views.places_visited, name= 'place_visited'),
    path('place/<int:place_pk>/was visited', views.place_was_visited, name = 'place was visited'),
    path('about', views.about, name='about')
]