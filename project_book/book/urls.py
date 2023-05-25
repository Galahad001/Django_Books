from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:pk>/', views.PostsView.as_view(), name='book'),
]

