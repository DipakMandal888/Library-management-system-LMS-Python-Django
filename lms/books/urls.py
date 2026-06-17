from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.books_list, name='list'),
    path('new/', views.book_create, name='create'),
    path('<int:pk>/', views.book_detail, name='detail'),
    path('<int:pk>/edit/', views.book_update, name='update'),
    path('<int:pk>/delete/', views.book_delete, name='delete'),
]
