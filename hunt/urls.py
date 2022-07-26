from django.urls import path
from . import views

app_name = 'hunt'

urlpatterns = [
    path('hunt/', views.hunt, name='hunt'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('gen_data/', views.gen_data, name='gen_data'),
]