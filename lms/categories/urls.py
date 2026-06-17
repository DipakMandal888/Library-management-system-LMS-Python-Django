from django.urls import path

from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.categories_list, name='list'),
    path('new/', views.category_create, name='create'),
    path('<int:pk>/', views.category_detail, name='detail'),
    path('<int:pk>/edit/', views.category_update, name='update'),
    path('<int:pk>/delete/', views.category_delete, name='delete'),
]
