
from django.urls import path
from . import views

app_name = 'pw'

urlpatterns = [
    path('', views.index_view),
    path('index', views.index_view),
    path('home', views.index_view, name='home'),
    path('about', views.about_view, name='sobre'),
]