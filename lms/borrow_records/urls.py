from django.urls import path

from . import views

app_name = 'borrow_records'

urlpatterns = [
    path('', views.borrow_records_list, name='list'),
    path('new/', views.borrow_record_create, name='create'),
    path('<int:pk>/', views.borrow_record_detail, name='detail'),
    path('<int:pk>/edit/', views.borrow_record_update, name='update'),
    path('<int:pk>/delete/', views.borrow_record_delete, name='delete'),
]
