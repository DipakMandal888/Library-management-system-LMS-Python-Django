from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.authors_list, name='list'),
    path('new/', views.author_create, name='create'),
    path('<int:pk>/', views.author_detail, name='detail'),
    path('<int:pk>/edit/', views.author_update, name='update'),
    path('<int:pk>/delete/', views.author_delete, name='delete'),
]
